"""Module to fetch query results
"""
import pycurl
import cStringIO
from minerva.common.constants import QUERY_TYPE, SINDICE_URL

class Fetcher(object):
    
    def __init__(self, logger):
        self.logger = logger
        
    def fetch(self, query_type, query, filter_query=None, page=1, format__='json'):
        curl = pycurl.Curl()
        buf = cStringIO.StringIO()
        sep = '&'
        query_post = SINDICE_URL + str(QUERY_TYPE[query_type]) + '=' + str(query) \
        + sep + 'page=' + str(page) + sep + 'format=' + format__
        if filter_query:
            query_post += sep + 'fq=' + filter_query
        self.logger.debug("Query URL: " + query_post)
        curl.setopt(pycurl.URL, query_post)
        curl.setopt(pycurl.WRITEFUNCTION, buf.write)
        try:
            curl.perform()
            if curl.getinfo(pycurl.HTTP_CODE) == 200:
                self.logger.debug('Query success!')
            else:
                self.logger.debug('Query Failure!')
            response = buf.getvalue()
            buf.close() 
            curl.close() 
            return response
        except pycurl.error, msg: 
            errno, text = msg 
            self.logger.error('pycURL Error! (error number %d): %s' % (errno, text))
            self.logger.error('pycURL HTTP status code: %d' % (curl.getinfo(pycurl.HTTP_CODE)))  
              
    