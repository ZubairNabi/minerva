import logging

def get_logger(logger_type):
    logger = logging.getLogger(logger_type)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s.%(funcName)s %(message)s')
    if logger_type == 'server':
        hdlr = logging.FileHandler('server.log')
    elif logger_type == 'client':
        hdlr = logging.FileHandler('client.log')
    elif logger_type == 'client_tests':
        hdlr = logging.FileHandler('client_tests.log')
        formatter = logging.Formatter('%(asctime)s %(message)s')
    else:
        return
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr) 
    logger.setLevel(logging.DEBUG)
    return logger
