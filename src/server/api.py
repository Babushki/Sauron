import cherrypy
from user_service import UserService, NazgulListService, AuthService
from process_service import ProcessService
from whitelist_service import WhitelistService
from screenshot_service import ScreenshotService, ScreenshotListService
from config import WITH_AUTHENTICATION, WITHOUT_AUTHENTICATION, CHERRYPY_CONFIG_DEFAULT


if __name__ == '__main__':
    cherrypy.config.update(CHERRYPY_CONFIG_DEFAULT)
    cherrypy.tree.mount(UserService(), '/api/user', WITH_AUTHENTICATION)
    cherrypy.tree.mount(NazgulListService(), '/api/nazgul', WITH_AUTHENTICATION)
    cherrypy.tree.mount(ProcessService(), '/api/process', WITH_AUTHENTICATION)
    cherrypy.tree.mount(WhitelistService(), '/api/whitelist', WITH_AUTHENTICATION)
    cherrypy.tree.mount(ScreenshotService(), '/api/screenshot', WITH_AUTHENTICATION)
    cherrypy.tree.mount(ScreenshotListService(), '/api/screenshotlist', WITH_AUTHENTICATION)
    cherrypy.tree.mount(AuthService(), '/api/auth', WITH_AUTHENTICATION)



    cherrypy.engine.start()
    cherrypy.engine.block()