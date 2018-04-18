import cherrypy
from database import MongoAPI
import json


@cherrypy.expose
class UserService:

    def GET(self):
        with MongoAPI(database='sauron', collection='users') as col:
            return json.dumps(col.get(None, True))

    @cherrypy.tools.json_in()
    def POST(self):
        request = cherrypy.request.json
        try:
            with MongoAPI(database='sauron', collection='users') as col:
                col.insert({'login': request['login'], 'password': request['password']})
        except KeyError:
            raise cherrypy.HTTPError(400, 'BAD REQUEST')


if __name__ == '__main__':
    cherrypy.config.update({
            'server.socket_host': '10.0.2.15',
            'server.socket_port': 8080,
        })

    cherrypy.quickstart(UserService(), '/users', {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})

