import base64

from fetch_query import Fetcher
from parse_query import Parser
from minerva.common.serialization import Serialization
import minerva.common.RSACrypto as RSA
from threading import Lock

import minerva.common.AESCrypto as AES
from ontology_manager import OntologyManager

class Handler(object):
    
    def __init__(self, logger, encryption):
        self.logger = logger
        self.encryption = encryption
        # contains RegisterAgent objects indexed by client_id
        self.clients = {}
        self.clients_lock = Lock()
        # contains registered user names for fast look up 
        self.registered_usernames = set()
        self.registered_usernames_lock = Lock()
        self.client_id = 0
        self.rsa_key = RSA.generate_RSA_keypair()
        self.logger.info('Server RSA key mod %s, exp %s', str(self.rsa_key.n), str(self.rsa_key.e))
        self.__fetch_query = Fetcher(logger)
        self.__parse_query = Parser(logger)
        self.__ontology_manager = OntologyManager()
        
    def handle_query(self, message):
        query_message = Serialization.deserialize_sendquery(message)
        self.clients_lock.acquire()
        if query_message.user_id in self.clients:
            aes_key = self.clients[query_message.user_id].symmetric_key
            self.clients_lock.release()
            query = query_message.query
            if self.encryption:
                query = AES._aes_decrypt_and_decode(aes_key, 
                                                    query_message.query)
        response = self.__fetch_query.fetch('keyword', query, page=query_message.page)
        entries = self.__parse_query.parse(response)
        if self.encryption:
            return AES._aes_encrypt_and_encode(aes_key, 
                                               Serialization.serialize_sendqueryresponse(entries))
        return base64.b64encode(Serialization.serialize_sendqueryresponse(entries))
    
    def handle_getpublickey(self, username):
        return base64.b64encode(Serialization.serialize_getpublickeyresponse(self.rsa_key))
    
    def handle_register(self, register):
        self.registered_usernames_lock.acquire()
        if register.username not in self.registered_usernames:
            self.registered_usernames.add(register.username)
            user_id = self.client_id
            self.registered_usernames_lock.release()
            if self.encryption:
                register.symmetric_key = RSA._rsa_decrypt_and_decode(self.rsa_key, 
                                                          register.symmetric_key)
            self.clients_lock.acquire()
            self.clients[user_id] = register
            self.client_id += 1  
            self.clients_lock.release()
            self.__ontology_manager.add_individual('User', register.username)
            self.__ontology_manager.save()
            self.logger.debug('Username %s registered and assigned ID %d' \
                              % (register.username, user_id))
            if self.encryption:
                self.clients_lock.acquire()
                ret = RSA.rsa_encrypt_client(self.clients[user_id], 
                                              Serialization.serialize_registeruserresponse(user_id))
                self.clients_lock.release()
                return ret
            return base64.b64encode(Serialization.serialize_registeruserresponse(user_id))
        self.logger.error('Username %s already registered' % register.username)
        return
                                
                                