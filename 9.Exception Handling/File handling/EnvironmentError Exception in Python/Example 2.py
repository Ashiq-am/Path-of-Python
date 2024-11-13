# importing the module
import os
import sys

try:
	for i in range(7):
		print(i)
		print(os.ttyname(i))
except Exception as e:
	print(e)
	print(sys.exc_info()[0])
