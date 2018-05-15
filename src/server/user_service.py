import cherrypy
from database_management import COLLECTIONS
from config import CHERRYPY_CONFIG_DEFAULT, WITHOUT_AUTHENTICATION
from base64 import b64encode


@cherrypy.expose
class UserService:

    @cherrypy.tools.json_out()
    def GET(self, login, password):
        with COLLECTIONS['users'] as col:
            user_exists = list(col.find({'login': login, 'password': password}))
            if user_exists:
                auth_token = b64encode(bytes(f'{login}:{password}', 'utf-8')).decode('utf-8')
                return {'auth_token': auth_token}
            else:
                raise cherrypy.HTTPError(404, 'User not found')

    @cherrypy.tools.json_in()
    def POST(self):
        request = cherrypy.request.json
        with COLLECTIONS['users'] as col:
            try:
                col.insert_one({'login': request['login'], 'password': request['password']})
            except(KeyError, TypeError) :
                raise cherrypy.HTTPError(400, 'Bad Request')


if __name__ == '__main__':
    cherrypy.config.update(CHERRYPY_CONFIG_DEFAULT)
    cherrypy.quickstart(UserService(), '/api/user', WITHOUT_AUTHENTICATION)

