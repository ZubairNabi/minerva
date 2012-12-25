import sys
sys.path.append("./../..")

import cherrypy
import base64

from minerva.common.serialization import Serialization
from handle_query import Handler
from minerva.common.constants import SERVER_PORT
from minerva.common.logger import get_logger

class Server():
    
    def __init__(self):
        
        self.__port = SERVER_PORT
        self.__addr = '0.0.0.0'
        cherrypy.config.update({
            'server.socket_port': self.__port,
            'server.socket_host': self.__addr,
        })
        self.logger = get_logger('server')
        self.logger.debug('Initialized cherrypy output server')
        
    def start(self):
        app_config = {'/':
            {   'tools.encode.on': True, 
                'tools.encode.encoding': 'utf-8',
                'tools.decode.on': True,
                'tools.trailing_slash.on': True,
            }
        }
        cherrypy.tree.mount(Root(self.logger), config=app_config)
        self.logger.debug('Started cherrypy output server engine')
        cherrypy.engine.start()
        cherrypy.engine.block()

class Root(object):

    def __init__(self, logger):
        self.logger = logger
        self.handler = Handler(logger)

    @cherrypy.expose
    def index(self):
        return "Hello world!\n"

    @cherrypy.expose
    def query(self, message):
        try:
            message = base64.b64decode(message)
            return self.handler.handle_query(message)
        
        except Exception, err_msg:
            cherrypy.response.status = 500
            self.logger.error("Error while serving client: %s" % \
            (str(err_msg)))
            
    @cherrypy.expose
    def register(self, message):
        try:
            message = base64.b64decode(message)
            register_message = Serialization.deserialize_registeruser(message)
            return self.handler.handle_register(register_message)
        
        except Exception, err_msg:
            cherrypy.response.status = 500
            self.logger.error("Error while serving client: %s" % \
            (str(err_msg)))
            
    @cherrypy.expose
    def getpublickey(self, message):
        try:
            message = base64.b64decode(message)
            getpublickey_message = Serialization.deserialize_getpublickey(message)
            return self.handler.handle_getpublickey(getpublickey_message.username)
        
        except Exception, err_msg:
            cherrypy.response.status = 500
            self.logger.error("Error while serving client: %s" % \
            (str(err_msg)))

def main():
    server = Server()
    server.start()

if __name__ == '__main__':
    main()
    