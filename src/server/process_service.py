import cherrypy
from database_management import COLLECTIONS
from config import CHERRYPY_CONFIG_DEFAULT, WITHOUT_AUTHENTICATION

@cherrypy.expose
class ProcessService:

    @cherrypy.tools.json_out()
    def GET(self, time_from = None, time_to = None, nazgul = None, group = None, limit = None):
        query = {}
        with COLLECTIONS['users'] as col:
            user = col.find_one({'login': cherrypy.request.login})
        if user['account_type'] in ('superadmin', 'user'):
            try:
                if time_from and time_to:
                    query.update({'create_time': {'$lt': int(time_to), '$gte': int(time_from)}})
                if nazgul:
                    query.update({'nazgul': str(nazgul)})
                if group:
                    query.update({'group': str(group)})

                with COLLECTIONS['processes'] as col:
                    if limit:
                        return list(col.find(query, {'_id': False}).limit(int(limit)))
                    else:
                        return list(col.find(query, {'_id': False}))
            except ValueError:
                raise cherrypy.HTTPError(400, 'Bad Request')
        else:
            raise cherrypy.HTTPError(401, 'Unauthorized')

    @cherrypy.tools.json_in()
    def POST(self):
        request = cherrypy.request.json
        with COLLECTIONS['users'] as col:
            user = col.find_one({'login': cherrypy.request.login})
        if user['account_type'] == 'nazgul':
            with COLLECTIONS['processes'] as col:
                try:
                    for r in request:
                        col.insert_one({
                            'create_time': r['create_time'],
                            'nazgul': cherrypy.request.login,
                            'processes': r['processes'],
                            'group': r['group'],
                        })
                except (KeyError, TypeError):
                    raise cherrypy.HTTPError(400, 'Bad Request')
        else:
            raise cherrypy.HTTPError(401, 'Unauthorized')
