from fetch_query import Fetcher
from parse_query import Parser
from minerva.common.serialization import Serialization

class Handler(object):
    
    def __init__(self):
        self.__fetch_query = Fetcher()
        self.__parse_query = Parser()
        
    def handle(self, query):
        response = self.__fetch_query.fetch('keyword', query, page=1)
        entries = self.__parse_query.parse(response)
        return Serialization.serialize_sendqueryresponse(entries)