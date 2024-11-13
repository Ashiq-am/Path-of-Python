# import modules
import numpy as np
import sys

# compute numpy performance
def np_performance():
	array = np.empty(100000000)
	for i in range(100000000):
		array[i] = i
	print("SIZE : ",
		sys.getsizeof(array)/1024.0**2,
		"MiB")

# compute dictionary performance
def dict_performance():
	dic = dict()
	for i in range(100000000):
		dic[i] = i
	print("SIZE : ",
		sys.getsizeof(dic)/1024.0**2,
		"MiB")
