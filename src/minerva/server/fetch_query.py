"""Module to fetch query results
"""
import pycurl
import cStringIO

QUERY_TYPE = { 'keyword': 'q',
                  'ntriple': 'nq'
            }

class Fetcher(object):
    
    def __init__(self):
        self.curl = pycurl.Curl()
        self.buf = cStringIO.StringIO()
        
    def fetch(self, query_type, query, filter_query=None, page=1, format__='json'):
        baseurl = "http://api.sindice.com/v3/search?"
        sep = '&'
        query_post = baseurl + str(QUERY_TYPE[query_type]) + '=' + str(query) \
        + sep + 'page=' + str(page) + sep + 'format=' + format__
        if filter_query:
            query_post += sep + 'fq=' + filter_query
        print "Query URL: " + query_post
        self.curl.setopt(pycurl.URL, query_post)
        self.curl.setopt(pycurl.WRITEFUNCTION, self.buf.write)
        try:
            self.curl.perform()
            if self.curl.getinfo(pycurl.HTTP_CODE) == 200:
                print 'Query success!'
            else:
                print 'Query Failure!'
            return self.buf.getvalue()
        except pycurl.error, msg: 
            errno, text = msg 
            print 'pycURL Error! (error number %d): %s' % (errno, text)
            print 'pycURL HTTP status code: %d' % (self.curl.getinfo(pycurl.HTTP_CODE))  
    
    def __del__(self):
        self.curl.close()  
        self.buf.close()   
    
def test():
    fetch_query = Fetcher()
    response = fetch_query.fetch('keyword', 'Islamabad')
    print response

if __name__ == '__main__':
    test()
    
    