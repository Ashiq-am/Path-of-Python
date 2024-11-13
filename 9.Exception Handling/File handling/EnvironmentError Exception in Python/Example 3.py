# importing the module
import sys
import os

try:
	# an invalid path
	os.rmdir('GEEKS')
except Exception as e:
	print(e)
	print(sys.exc_info()[0])
