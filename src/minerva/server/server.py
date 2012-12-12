import cherrypy

from minerva.common.serialization import Serialization
from handle_query import Handler

class OutputServer():
    
    def __init__(self):
        
        self.__port = 8080
        self.__addr = "0.0.0.0"
        cherrypy.config.update({
            'server.socket_port': self.__port,
            'server.socket_host': self.__addr,
        })
        print 'Initialized cherrypy output server'
        
    def start(self):
        app_config = {'/':
            {   'tools.encode.on': True, 
                'tools.encode.encoding': 'utf-8',
                'tools.decode.on': True,
                'tools.trailing_slash.on': True,
            }
        }
        cherrypy.tree.mount(Root(), config=app_config)
        cherrypy.engine.start() 
        print 'Started cherrypy output server engine'

class Root(object):

    def __init__(self):
        self.handler = Handler()

    @cherrypy.expose
    def index(self):
        return "Hello world!\n"

    @cherrypy.expose
    def query(self, message):
        try:
            query_message = Serialization.deserialize_sendquery(message)
            return self.handler.handle(query_message.query)
        
        except Exception, err_msg:
            cherrypy.response.status = 500
            print "Error while serving client %s, query %s: %s" % \
            (str(query_message.user_id), query_message.query, str(err_msg))

def main():
    output_server = OutputServer()
    output_server.start()

if __name__ == '__main__':
    main()
    