import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.sep + '../..')
import random


from minerva.common.constants import SERVER_IP, ENCRYPTION, VIDEO_URL
from minerva.client.client import Client
from minerva.common.logger import get_logger
from minerva.tests.client_tests import execute_and_time


def register_and_fetch_binary(argv):
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
    execute_and_time(client.fetch_binary, logger, args=[VIDEO_URL])
    

if __name__ == '__main__':
    register_and_fetch_binary(sys.argv)
    