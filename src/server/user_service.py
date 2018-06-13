import cherrypy
from database_management import COLLECTIONS
from config import CHERRYPY_CONFIG_DEFAULT, WITHOUT_AUTHENTICATION
from base64 import b64encode


@cherrypy.expose
class UserService:

    @cherrypy.tools.json_out()
    def GET(self):
        with COLLECTIONS['users'] as col:
            user = col.find_one({'login': cherrypy.request.login})
        if user['account_type'] in ('superadmin',):
            with COLLECTIONS['users'] as col:
                users = list(col.find({}, {'_id': False}))
            return users
        else:
            raise cherrypy.HTTPError(401, 'Unauthorized')

    @cherrypy.tools.json_in()
    def POST(self):
        with COLLECTIONS['users'] as col:
            try:
                user = col.find_one({'login': cherrypy.request.login})
                if user['account_type'] == 'superadmin':
                    request = cherrypy.request.json
                    duplicate = col.find_one({'login': request['login']})
                    if duplicate:
                        raise cherrypy.HTTPError(409, 'Login already in use')
                    col.insert_one({'login': request['login'], 'password': request['password'], 'account_type': request['account_type']})
                else:
                    raise cherrypy.HTTPError(401, 'Unauthorized')
            except(KeyError, TypeError):
                raise cherrypy.HTTPError(400, 'Bad Request')


    @cherrypy.tools.json_in()
    def PUT(self, login):
        request = cherrypy.request.json
        with COLLECTIONS['users'] as col:
            try:
                user = col.find_one({'login': cherrypy.request.login})
                if user['account_type'] == 'superadmin':
                    col.update_many({'login': login}, {'$set': {'password': request['password'], 'account_type': request['account_type']}})
                else:
                    raise cherrypy.HTTPError(401, 'Unauthorized')
            except(KeyError, TypeError) :
                raise cherrypy.HTTPError(400, 'Bad Request')

    def DELETE(self, login):
        with COLLECTIONS['users'] as col:
            user = col.find_one({'login': cherrypy.request.login})
            if user['account_type'] == 'superadmin':
                col.delete_many({'login': login})
            else:
                raise cherrypy.HTTPError(401, 'Unauthorized')

@cherrypy.expose
class NazgulListService:

    @cherrypy.tools.json_out()
    def GET(self, time_from, time_to = None, group = None):
        with COLLECTIONS['users'] as col:
            user = col.find_one({'login': cherrypy.request.login})
        if user['account_type'] in ('superadmin', 'user'):
            query = {}
            if time_to:
                query.update({'create_time': {'$lt': int(time_to), '$gte': int(time_from)}})
            else:
                query.update({'create_time': {'$gte': int(time_from)}})
            if group:
                query.update({'group': str(group)})

            with COLLECTIONS['processes'] as col:
                processes = list(col.find(query, {'_id': False}))
            users = set()
            for p in processes:
                users.add(p['nazgul'])
            return list(users)


@cherrypy.expose
class AuthService:
    def GET(self):
        with COLLECTIONS['users'] as col:
            user = col.find_one({'login': cherrypy.request.login})
        if user['account_type'] not in ('superadmin', 'user', 'nazgul'):
            raise cherrypy.HTTPError(401, 'Unauthorized')