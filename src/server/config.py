import cherrypy
from database_management import COLLECTIONS

def validate_password(realm, login, password):
    with COLLECTIONS['users'] as col:
        user_exists = list(col.find({'login': login, 'password': password}))
    return bool(user_exists)

CHERRYPY_CONFIG_DEFAULT = {
    'server.socket_host': '10.0.2.15',
    'server.socket_port': 8080,
    'tools.auth_basic.on': True,
    'tools.auth_basic.realm': '10.0.2.15',
    'tools.auth_basic.checkpassword': validate_password,
}

WITHOUT_AUTHENTICATION = {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher(), 'tools.auth_basic.on': False}}
WITH_AUTHENTICATION = {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
