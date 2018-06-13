import cherrypy
from database_management import COLLECTIONS
from config import CHERRYPY_CONFIG_DEFAULT, WITHOUT_AUTHENTICATION
from base64 import b64encode

@cherrypy.expose
class ScreenshotService:

    @cherrypy.tools.json_out()
    def GET(self, filename):
        with COLLECTIONS['users'] as col:
            user = col.find_one({'login': cherrypy.request.login})
        if user['account_type'] in ('user', 'superadmin'):
            file = open('/screenshots/' + filename, 'rb')
            data = file.read()
            file.close()
            encoded = b64encode(data)
            return {'screenshot': str(encoded)}
        else:
            raise cherrypy.HTTPError(401, 'Unauthorized')

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
        else:
            raise cherrypy.HTTPError(401, 'Unauthorized')

@cherrypy.expose
class ScreenshotListService:

    @cherrypy.tools.json_out()
    def GET(self, time_from = None, time_to = None, nazgul = None, group = None, newest = False):
        with COLLECTIONS['users'] as col:
            user = col.find_one({'login': cherrypy.request.login})
        if user['account_type'] in ('nazgul', 'superadmin'):
            query = {}
            if time_from and time_to:
                query.update({'create_time': {'$lt': int(time_to), '$gte': int(time_from)}})
            if nazgul:
                query.update({'nazgul': str(nazgul)})
            if group:
                query.update({'group': str(group)})
            #TODO
        else:
            raise cherrypy.HTTPError(401, 'Unauthorized')
