# -*- coding=UTF-8 -*-
import random,logging
for i in  range(random.randint(1,20)):
    print i
from log import Logger
logger = Logger(logger="BasePage").getlog()
logger.info("hello world")
import sys
print('Python %s on %s' % (sys.version, sys.platform))
file=sys.path.extend('F:\PycharmProjects')
print file
# sys.path.extend([WORKING_DIR_AND_PYTHON_PATHS])


