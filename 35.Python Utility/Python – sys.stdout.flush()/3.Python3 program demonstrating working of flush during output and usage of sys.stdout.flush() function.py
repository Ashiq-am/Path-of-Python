# Python3 program demonstrating working
# of flush during output and usage of
# sys.stdout.flush() function

import sys
import time

for i in range(10):
	print(i, end =' ')
	sys.stdout.flush()
	time.sleep(1)
