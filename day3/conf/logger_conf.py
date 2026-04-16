#configure log format

import logging

def setup_logger():

    #creating a logger for the healthcare application

    logger = logging.getLogger('healthacre_logger')
    logger.setLevel(logging.DEBUG)
    
    #check if the logger exists and has handlers to avoid adding multiple handlers

    if logger.hasHandlers():
        return logger

    #create file handler to write logs to a healthcare.log file
    
    file_handler = logging.FileHandler('healthcare.log')
    logger.setLevel(logging.DEBUG)

    #setting a format for the logging

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger