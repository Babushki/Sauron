import cherrypy
from database_management import COLLECTIONS
from config import CHERRYPY_CONFIG_DEFAULT, WITHOUT_AUTHENTICATION
from base64 import b64encode


@cherrypy.expose
class WhitelistService:

    @cherrypy.tools.json_out()
    def GET(self, only_active = True):
        try:
            query = {'active': True} if bool(int(only_active)) else {}
        except ValueError:
            raise cherrypy.HTTPError(400, 'Bad Request')
        with COLLECTIONS['whitelists'] as col:
            return list(col.find(query, {'_id': False}))

    @cherrypy.tools.json_in()
    def POST(self):
        request = cherrypy.request.json
        with COLLECTIONS['whitelists'] as col:
            try:
                col.insert_one({
                    'name': request['name'],
                    'active': False,
                    'processes': request['processes'],
                    'domains': request['domains'],
                })
            except (KeyError, TypeError):
                raise cherrypy.HTTPError(400, 'Bad Request')

    def PATCH(self, name, active):
        with COLLECTIONS['whitelists'] as col:
            try:
                col.update_many({'name': name}, {'$set': {'active': bool(int(active))}})
            except ValueError:
                raise cherrypy.HTTPError(400, 'Bad Request')


if __name__ == '__main__':
    cherrypy.config.update(CHERRYPY_CONFIG_DEFAULT)
    cherrypy.quickstart(WhitelistService(), '/api/whitelist', WITHOUT_AUTHENTICATION)