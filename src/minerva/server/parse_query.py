try: import simplejson
except: import json

from fetch_query import Fetcher

class Parser():
    
    def __init__(self, logger):
        self.logger = logger
    
    def parse(self, query):
        query = json.loads(query)
        entries = []
        for entry in query['entries']:
            entries.append(((entry['title'][0]['value']), entry['link']))
        return entries
        
def test():
    fetch_query = Fetcher()
    response = fetch_query.fetch('keyword', 'Islamabad', page=2)
    parse_query = Parser()
    entries = parse_query.parse(response)
    for entry in entries:
        print entry

if __name__ == '__main__':
    test()