import logging

def get_logger(logger_type):
    logger = logging.getLogger(logger_type)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s.%(funcName)s %(message)s')
    if logger_type == 'server':
        hdlr = logging.FileHandler('server.log')
    elif logger_type == 'client':
        hdlr = logging.FileHandler('client.log')
    else:
        hdlr = logging.FileHandler(logger_type + '.log')
        formatter = logging.Formatter('%(asctime)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr) 
    logger.setLevel(logging.DEBUG)
    return logger