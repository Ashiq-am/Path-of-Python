# Python3 program demonstrating working
# of flush during output and usage of
# flush parameter of print statement

import sys
import time

for i in range(10):
	print(i, end =' ', flush = True)
	time.sleep(1)
