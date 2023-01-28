import logging


# logging.basicConfig(filename="..\\Logs\\logfile.log",format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'
#                     ,level=logging.INFO)
# log = logging.getLogger()
#
# log.info("This is our first log")

def log():
    logging.basicConfig(filename=".\\Logs\\logfile.log", format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p'
                        , level=logging.INFO)
    logger = logging.getLogger()
    return logger


logger = log()
logger.info("This is a new log")
logger.error("This is an error message")

