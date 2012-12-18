"""Module to fetch query results
"""
import pycurl
import cStringIO
from minerva.common.constants import QUERY_TYPE, SINDICE_URL

class Fetcher(object):
    
    def __init__(self, logger):
        self.curl = pycurl.Curl()
        self.logger = logger
        
    def fetch(self, query_type, query, filter_query=None, page=1, format__='json'):
        buf = cStringIO.StringIO()
        sep = '&'
        query_post = SINDICE_URL + str(QUERY_TYPE[query_type]) + '=' + str(query) \
        + sep + 'page=' + str(page) + sep + 'format=' + format__
        if filter_query:
            query_post += sep + 'fq=' + filter_query
        self.logger.debug("Query URL: " + query_post)
        self.curl.setopt(pycurl.URL, query_post)
        self.curl.setopt(pycurl.WRITEFUNCTION, buf.write)
        try:
            self.curl.perform()
            if self.curl.getinfo(pycurl.HTTP_CODE) == 200:
                self.logger.debug('Query success!')
            else:
                self.logger.debug('Query Failure!')
            response = buf.getvalue()
            buf.close() 
            return response
        except pycurl.error, msg: 
            errno, text = msg 
            self.logger.error('pycURL Error! (error number %d): %s' % (errno, text))
            self.logger.error('pycURL HTTP status code: %d' % (self.curl.getinfo(pycurl.HTTP_CODE)))  
    
    def __del__(self):
        self.curl.close()    
    
def test():
    fetch_query = Fetcher()
    response = fetch_query.fetch('keyword', 'Islamabad')
    print response

if __name__ == '__main__':
    test()
    
    