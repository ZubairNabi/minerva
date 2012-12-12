"""Module to fetch query results
"""
import pycurl
import cStringIO

from minerva.common.serialization import Serialization

QUERY_TYPE = { 'keyword': 'q',
                  'ntriple': 'nq'
            }

class Fetcher(object):
    
    def __init__(self, ip, port):
        self.curl = pycurl.Curl()
        self.buf = cStringIO.StringIO()
        self.server_ip = ip
        self.server_port = port
        
    def fetch(self, query):
        method = 'query'
        query_var = 'message'
        base_url = 'http://' + self.server_ip + ':' + str(self.server_port)
        encoded = Serialization.serialize_sendquery(1, query)
        service_url = '/' + method + '/?' + query_var + '=' + encoded
        print 'URL: %s', base_url + service_url
        self.curl.setopt(pycurl.URL, base_url + service_url)
        self.curl.setopt(pycurl.WRITEFUNCTION, self.buf.write)
        try:
            self.curl.perform()
            if self.curl.getinfo(pycurl.HTTP_CODE) == 200:
                print 'Query success!'
            else:
                print 'Query Failure!'
            return Serialization.deserialize_sendqueryresponse(self.buf.getvalue())
        except pycurl.error, msg: 
            errno, text = msg 
            print 'pycURL Error! (error number %d): %s' % (errno, text)
            print 'pycURL HTTP status code: %d' % (self.curl.getinfo(pycurl.HTTP_CODE))  
    
    def __del__(self):
        self.curl.close()  
        self.buf.close()   
    
def test():
    fetch_query = Fetcher("localhost", 8080)
    response = fetch_query.fetch('Islamabad')
    print response

if __name__ == '__main__':
    test()
    
    