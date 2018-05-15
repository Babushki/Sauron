import cherrypy
from user_service import UserService
from process_service import ProcessService
from config import WITH_AUTHENTICATION, WITHOUT_AUTHENTICATION, CHERRYPY_CONFIG_DEFAULT


if __name__ == '__main__':
    cherrypy.config.update(CHERRYPY_CONFIG_DEFAULT)
    cherrypy.quickstart(UserService(), '/api/user', WITHOUT_AUTHENTICATION)
    cherrypy.quickstart(ProcessService(), '/api/process', WITH_AUTHENTICATION)