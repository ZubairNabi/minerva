try: import simplejson
except: import json

class Parser():
    
    def __init__(self, logger):
        self.logger = logger
    
    def parse(self, query):
        query = json.loads(query)
        entries = []
        for entry in query['entries']:
            entries.append(((entry['title'][0]['value']), entry['link']))
        return entries