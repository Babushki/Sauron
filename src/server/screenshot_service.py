import cherrypy
from database_management import COLLECTIONS
from config import CHERRYPY_CONFIG_DEFAULT, WITHOUT_AUTHENTICATION

@cherrypy.expose
class ScreenshotService:

    @cherrypy.tools.json_out()
    def GET(self, time_from = None, time_to = None, nazgul = None, group = None, limit = 20):
        pass

    def POST(self, screenshot, create_time, nazgul, group):
        filename = group + '_' + nazgul + '_' + create_time
        with COLLECTIONS['users'] as col:
            user = col.find_one({'login': cherrypy.request.login})
        if user['account_type'] in ('nazgul', 'superadmin'):

            data = screenshot.file.read()

            file = open('/screenshots/' + filename, 'wb')
            file.write(data)
            file.close()

            with COLLECTIONS['screenshots'] as col:
                col.insert_one({
                    'filename': filename,
                    'group': group,
                    'nazgul': nazgul,
                    'create_time': int(create_time),
                })