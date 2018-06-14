import cherrypy
from database_management import COLLECTIONS
from config import CHERRYPY_CONFIG_DEFAULT, WITHOUT_AUTHENTICATION
from base64 import b64encode
import string
import random


@cherrypy.expose
class WhitelistService:

    @cherrypy.tools.json_out()
    def GET(self, only_active = True, group = None, user = None):
        with COLLECTIONS['users'] as col:
            user_account = col.find_one({'login': cherrypy.request.login})
        if user_account['account_type'] in ('superadmin', 'user', 'nazgul'):
            try:
                query = {'active': True} if bool(int(only_active)) else {}
                if group:
                    query.update({'group': str(group)})
                if user:
                    query.update({'user': str(user)})
            except ValueError:
                raise cherrypy.HTTPError(400, 'Bad Request')
            with COLLECTIONS['whitelists'] as col:
                return list(col.find(query, {'_id': False}))
        else:
            raise cherrypy.HTTPError(401, 'Unauthorized')

    @cherrypy.tools.json_in()
    def POST(self):
        with COLLECTIONS['users'] as col:
            user = col.find_one({'login': cherrypy.request.login})
        if user['account_type'] in ('superadmin', 'user'):
            request = cherrypy.request.json
            while True:
                id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=30))
                with COLLECTIONS['whitelists'] as col:
                    duplicate = col.find_one({'id': id})
                if not duplicate:
                    break
            with COLLECTIONS['whitelists'] as col:
                try:
                    col.insert_one({
                        'name': request['name'],
                        'active': False,
                        'processes': request['processes'],
                        'group': request['group'],
                        'user': cherrypy.request.login,
                        'id': id,
                    })
                except (KeyError, TypeError):
                    raise cherrypy.HTTPError(400, 'Bad Request')
        else:
            raise cherrypy.HTTPError(401, 'Unauthorized')

    def PATCH(self, id, active):
        with COLLECTIONS['users'] as col:
            user = col.find_one({'login': cherrypy.request.login})
        if user['account_type'] in ('superadmin', 'user'):
            with COLLECTIONS['whitelists'] as col:
                try:
                    col.update_many({'id': id}, {'$set': {'active': bool(int(active))}})
                except ValueError:
                    raise cherrypy.HTTPError(400, 'Bad Request')
        else:
            raise cherrypy.HTTPError(401, 'Unauthorized')
