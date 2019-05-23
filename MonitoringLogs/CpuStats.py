#logfile = open(log, "w")
#with open(log, 'a') as logfile:
#    logfile.write(sttime + error + '\n')

import logging
import os
import subprocess

logger = logging.getLogger("test") #Module Level looger
#logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logging.basicConfig(level=logging.DEBUG,filename='myapp1.log',filemode='w',format='%(asctime)s %(message)s')

#create format
LOG_DATEFORMAT='%Y-%m-%d %H:%M:%S'
#LOG_FMT=('\n[%(levelname)s/%(name)s:%(lineno)d] %(asctime)s ' +
#              '(%(processName)s/%(threadName)s)\n> %(message)s')
#LOG_FMT=('\n[%(levelname)s:%(lineno)d] %(asctime)s ' + '(%(message)s')
LOG_FMT_TIME='%(asctime)s'
FORMATTER = logging.Formatter(LOG_FMT_TIME, datefmt=LOG_DATEFORMAT)

#CH = logging.StreamHandler()  # create console handler
#CH.setLevel(logging.DEBUG)  # set handler level to debug
#CH.setFormatter(FORMATTER)  # add formatter to ch
#logger.addHandler(CH)  # add console handler to logger

# FH = logging.FileHandler('myapp1.log')  # create file handler
# FH.setLevel(logging.DEBUG)  # set handler level to debug
# FH.setFormatter(FORMATTER)  # add formatter to fh
# logger.addHandler(FH)  # add file handler to logger
logger.info('CPU Stats,Trying Now')


# def setup_custom_logger(name):
#     formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
#                                   datefmt='%Y-%m-%d %H:%M:%S')
#     handler = logging.FileHandler('log.txt', mode='w')
#     handler.setFormatter(formatter)
#     screen_handler = logging.StreamHandler(stream=sys.stdout)
#     screen_handler.setFormatter(formatter)
#     logger = logging.getLogger(name)
#     logger.setLevel(logging.DEBUG)
#     logger.addHandler(handler)
#     logger.addHandler(screen_handler)
#     return logger

p1 = subprocess.Popen(['ls' , '-lrth'],stdout=subprocess.PIPE)
output = p1.communicate()

print output
