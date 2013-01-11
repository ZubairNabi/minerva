from Crypto.Cipher import AES

SERVER_IP = 'localhost'
SERVER_PORT = 8080
SINDICE_URL = "http://api.sindice.com/v3/search?"
QUERY_TYPE = { 'keyword': 'q',
                  'ntriple': 'nq'
            }
RSA_KEYSIZE = 1024
AES_KEYSIZE = 16
AES_MODE = AES.MODE_ECB
ONTOLOGY_FILE = "minerva.owl"
ENCRYPTION = True
POX_DIR = '/home/mininet/pox'