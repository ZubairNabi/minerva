import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.sep + '../..')
import time

from minerva.common.RSACrypto import generate_public_key, generate_RSA_keypair, \
get_public_key
from minerva.common.AESCrypto import generate_AES_key
from minerva.common.constants import SERVER_IP, SERVER_PORT, ENCRYPTION
from fetch_query import Fetcher
from minerva.common.serialization import Serialization
from minerva.common.logger import get_logger

class Client(object):
    
    def __init__(self, server_ip, encryption):
        self.rsa_key = generate_RSA_keypair()
        self.aes_key = generate_AES_key()
        self.logger = get_logger('client')
        self.server_public_key = None
        self.user_id = None
        self.__fetcher = Fetcher(server_ip, SERVER_PORT, self.rsa_key, self.aes_key, self.logger, encryption)
        self.username = 'zubair'
        self.user = Serialization.create_user(25, 'CS', 'MPhil', '2012')
        self.mobile_device = Serialization.create_mobiledevice('Samsung', 'Ace', True, True, 'Android', 'Gingerbread')
        self.network_details = Serialization.create_networkdetails(1000)
    
    def fetch(self, query, page):
        return self.__fetcher.fetch(self.user_id, query, page)
    
    def getpublickey(self):
        publickey = self.__fetcher.getpublickey(self.username).public_key
        self.server_public_key = generate_public_key(publickey.mod, publickey.exp)
        self.__fetcher.set_server_public_key(self.server_public_key)
        
    def register(self):
        self.user_id = self.__fetcher.register(self.username,
                                       self.user,
                                       self.mobile_device,
                                       self.network_details,
                                       get_public_key(self.rsa_key),
                                       self.aes_key).user_id
        
if __name__ == '__main__':
    server_ip = SERVER_IP
    encryption = ENCRYPTION
    if len(sys.argv) == 2:
        server_ip = sys.argv[1]
    elif len(sys.argv) == 3:
        server_ip = sys.argv[1]
        encryption = False
    logger = get_logger('client_tests')
    client = Client(server_ip, encryption)
    start_time = time.time()
    client.getpublickey()
    logger.info("getpublickey() took %f" % (time.time() - start_time))
    start_time = time.time()
    client.register()
    logger.info("register() took %f" % (time.time() - start_time))
    print "User ID: %d" % client.user_id
    start_time = time.time()
    print client.fetch("Islamabad", 1)
    logger.info("fetch() took %f" % (time.time() - start_time))
    start_time = time.time()
    print client.fetch("Islamabad", 2)
    logger.info("fetch() took %f" % (time.time() - start_time))
    
    