import sys
sys.path.append("./../..")

from minerva.common.RSACrypto import generate_public_key, generate_RSA_keypair, \
get_public_key
from minerva.common.AESCrypto import generate_AES_key
from minerva.common.constants import SERVER_IP, SERVER_PORT
from fetch_query import Fetcher
from minerva.common.serialization import Serialization

class Client(object):
    
    def __init__(self):
        self.rsa_key = generate_RSA_keypair()
        self.aes_key = generate_AES_key()
        self.server_public_key = None
        self.user_id = None
        self.__fetcher = Fetcher(SERVER_IP, SERVER_PORT, self.rsa_key, self.aes_key)
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
    client = Client()
    client.getpublickey()
    client.register()
    print client.user_id
    print client.fetch("Islamabad", 1)
    print client.fetch("Islamabad", 2)
    
    