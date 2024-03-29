import time
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.sep + '../..')
import random


from minerva.common.constants import SERVER_IP, ENCRYPTION
from minerva.client.client import Client
from minerva.common.logger import get_logger

def execute_and_time(method, logger, args=[]):
    start_time = time.time()
    if len(args) == 0:
        ret = method()
    elif len(args) == 1:
        ret = method(args[0])
    else:
        ret = method(args[0], args[1])
    if ret:
        print ret
    logger.info("%s took %f" % (method.__name__, (time.time() - start_time)))

def register_and_fetch_log(argv):
    server_ip = SERVER_IP
    encryption = ENCRYPTION
    log_file = 'client_test'
    if len(argv) == 2:
        server_ip = argv[1]
    elif len(argv) == 3:
        server_ip = argv[1]
        log_file = argv[2]
    elif len(argv) == 4:
        server_ip = argv[1]
        log_file = argv[2]
        encryption = False
    logger = get_logger(log_file)
    client = Client(server_ip, encryption)
    execute_and_time(client.getpublickey, logger)
    execute_and_time(client.register, logger)
    print "User ID: %d" % client.user_id
    execute_and_time(client.fetch, logger, args=["Islamabad", 1])
    execute_and_time(client.fetch, logger, args=["Islamabad", 2])
    
def register_and_fetch(argv):
    server_ip = SERVER_IP
    encryption = ENCRYPTION
    log_file = 'client_test'
    if len(argv) == 2:
        server_ip = argv[1]
    elif len(argv) == 3:
        server_ip = argv[1]
        log_file = argv[2]
    elif len(argv) == 4:
        server_ip = argv[1]
        log_file = argv[2]
        encryption = False
    logger = get_logger(log_file)
    client = Client(server_ip, encryption, '%010x' % random.randrange(256**5))
    client.getpublickey()
    client.register()
    execute_and_time(client.fetch, logger, args=["Islamabad", 1])
    

if __name__ == '__main__':
    register_and_fetch(sys.argv)
    