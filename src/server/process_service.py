import cherrypy
from database_management import COLLECTIONS
from config import CHERRYPY_CONFIG_DEFAULT, WITHOUT_AUTHENTICATION

@cherrypy.expose
class ProcessService:

    @cherrypy.tools.json_out()
    def GET(self, time_from = None, time_to = None, nazgul = None, limit = 20):
        query = {}
        try:
            if time_from and time_to:
                query.update({'create_time': {'$lt': int(time_to), '$gte': int(time_from)}})
            if nazgul:
                query.update({'nazgul': str(nazgul)})

            with COLLECTIONS['processes'] as col:
                return list(col.find(query, {'_id': False}).limit(int(limit)))
        except ValueError:
            raise cherrypy.HTTPError(400, 'Bad Request')

    @cherrypy.tools.json_in()
    def POST(self):
        request = cherrypy.request.json

        with COLLECTIONS['processes'] as col:
            try:
                col.insert_one({
                    'create_time': request['create_time'],
                    'nazgul': request['nazgul'],
                    'processes': request['processes'],
                    'group': request['group'],
                    'screenshot': request.get('screenshot')
                })
            except (KeyError, TypeError):
                raise cherrypy.HTTPError(400, 'Bad Request')


if __name__ == '__main__':
    cherrypy.config.update(CHERRYPY_CONFIG_DEFAULT)
    cherrypy.quickstart(ProcessService(), '/api/process', WITHOUT_AUTHENTICATION)