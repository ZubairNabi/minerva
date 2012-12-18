import base64

from fetch_query import Fetcher
from parse_query import Parser
from minerva.common.serialization import Serialization
import minerva.common.RSACrypto as RSA
import minerva.common.AESCrypto as AES

class Handler(object):
    
    def __init__(self, logger):
        self.logger = logger
        self.clients = {}
        self.client_id = 0
        self.rsa_key = RSA.generate_RSA_keypair()
        self.logger.info('Server RSA key mod %s, exp %s', str(self.rsa_key.n), str(self.rsa_key.e))
        self.__fetch_query = Fetcher(logger)
        self.__parse_query = Parser(logger)
        
    def handle_query(self, message):
        query_message = Serialization.deserialize_sendquery(message)
        if query_message.user_id in self.clients:
            aes_key = self.clients[query_message.user_id].symmetric_key
            query = AES._aes_decrypt_and_decode(aes_key, 
                                                  query_message.query)
        response = self.__fetch_query.fetch('keyword', query, page=1)
        entries = self.__parse_query.parse(response)
        return AES._aes_encrypt_and_encode(aes_key, Serialization.serialize_sendqueryresponse(entries))
    
    def handle_getpublickey(self, username):
        return base64.b64encode(Serialization.serialize_getpublickeyresponse(self.rsa_key))
    
    def handle_register(self, register):
        user_id = self.client_id
        register.symmetric_key = RSA._rsa_decrypt_and_decode(self.rsa_key, 
                                                  register.symmetric_key)
        self.clients[user_id] = register
        self.client_id += 1  
        return RSA.rsa_encrypt_client(self.clients[user_id], 
                                      Serialization.serialize_registeruserresponse(user_id))
                                
                                