"""Module to fetch query results
"""
import pycurl
import cStringIO
import base64

from minerva.common.serialization import Serialization
from minerva.common.logger import get_logger
import minerva.common.AESCrypto as AES
import minerva.common.RSACrypto as RSA

QUERY_TYPE = {  'keyword': 'q',
                'ntriple': 'nq'
}

class Fetcher(object):
    
    def __init__(self, ip, port, rsa_key, aes_key):
        self.curl = pycurl.Curl()
        self.server_ip = ip
        self.server_port = port
        self.rsa_key = rsa_key
        self.aes_key = aes_key
        self.server_public_key = None
        self.logger = get_logger('client')
        
    def set_server_public_key(self, server_public_key):
        self.server_public_key = server_public_key
        
    def __post(self, method, encoded_message, rsa_encrypt=None, aes_encrypt=None):
        buf = cStringIO.StringIO()
        query_var = 'message'
        base_url = 'http://' + self.server_ip + ':' + str(self.server_port)
        encoded_message = base64.b64encode(encoded_message)
        service_url = '/' + method + '/?' + query_var + '=' + encoded_message
        self.logger.debug('URL: %s', base_url + service_url)
        self.curl.setopt(pycurl.URL, base_url + service_url)
        self.curl.setopt(pycurl.WRITEFUNCTION, buf.write)
        try:
            self.curl.perform()
            if self.curl.getinfo(pycurl.HTTP_CODE) == 200:
                self.logger.debug('Query success!')
            else:
                self.logger.debug('Query Failure!')
            response = buf.getvalue()
            response = base64.b64decode(response)
            buf.close()
            if rsa_encrypt:
                response = RSA._rsa_decrypt(self.rsa_key, response)
            elif aes_encrypt:
                response = AES._aes_decrypt(self.aes_key, response)
            return response
        except pycurl.error, msg: 
            errno, text = msg 
            self.logger.error('pycURL Error! (error number %d): %s' % (errno, text))
            self.logger.error('pycURL HTTP status code: %d' % (self.curl.getinfo(pycurl.HTTP_CODE)))  
        
    def fetch(self, user_id, query, page):
        encoded = Serialization.serialize_sendquery(user_id, 
                                                    AES._aes_encrypt_and_encode(self.aes_key, query),
                                                    page)
        response = self.__post('query', encoded, aes_encrypt=True)
        return Serialization.deserialize_sendqueryresponse(response)
    
    def register(self, username, user, mobile_device, network_details, public_key, symmetric_key):
        encoded = Serialization.serialize_registeruser(username, 
                                                       user, 
                                                       mobile_device, 
                                                       network_details, 
                                                       str(public_key.n),
                                                       str(public_key.e),
                                                       RSA._rsa_encrypt_and_encode(self.server_public_key, symmetric_key))
        response = self.__post('register', encoded, rsa_encrypt=True)
        return Serialization.deserialize_registeruserresponse(response)
    
    def getpublickey(self, username):
        encoded = Serialization.serialize_getpublickey(username)
        response = self.__post('getpublickey', encoded)
        return Serialization.deserialize_getpublickeyresponse(response)

    def __del__(self):
        self.curl.close()    
    