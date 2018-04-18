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

# start tracking lap times
try:
	while True:
		input()
		lapTime = round( time.time() - lastTime, 2 )
		totalTime = round( time.time() - startTime, 2 )
		print( 'Lap #%s: %s (%s)' % (str(lapNum).rjust(3),str(totalTime).rjust(5).ljust(6),str(lapTime).rjust(5)), end=' ' )
		lapNum +=1
		lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
	# handle the Ctrl-C exception to keep its error message from displaying
	print('\nDone.')

