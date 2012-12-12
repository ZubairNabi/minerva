import base64

import messages_pb2 as messages

class Serialization(object):
    
    @staticmethod        
    def serialize_sendquery(user_id, query):
        send_query = messages.SendQuery()
        send_query.user_id = user_id
        send_query.query = query
        return base64.b64encode(send_query.SerializeToString())
    
    @staticmethod
    def deserialize_sendquery(serialized):
        decoded = base64.b64decode(serialized)
        send_query = messages.SendQuery()
        send_query.ParseFromString(decoded) 
        return send_query
    
    @staticmethod        
    def serialize_sendqueryresponse(results):
        send_query_response = messages.SendQueryResponse()
        for result in results:
            query_result = send_query_response.query_result.add()
            query_result.title = result[0]
            query_result.url = result[1]
        return base64.b64encode(send_query_response.SerializeToString())
    
    @staticmethod
    def deserialize_sendqueryresponse(serialized):
        decoded = base64.b64decode(serialized)
        send_query_response = messages.SendQueryResponse()
        send_query_response.ParseFromString(decoded) 
        return send_query_response
    
  