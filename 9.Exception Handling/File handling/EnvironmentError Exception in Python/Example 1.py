# importing the module
import sys

try:
	# an invalid path
	file = open("GeeksforGeeks.txt", 'r')
except Exception as e:
	print(e)
	print(sys.exc_info()[0])
