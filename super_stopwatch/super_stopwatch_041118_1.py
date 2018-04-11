# -*- coding: utf-8 -*-

#! python3

# USAGE
# python3 super_stopwatch_041118_1.py

import time

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
# logging.disable(logging.CRITICAL)

# show program instructions
print("""
	Press ENTER to start.  After, press ENTER to 'click' the stopwatch.\n
	Press Ctrl-C to quit.
	""")

input() # press Enter to begin
print('Started')

startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1

