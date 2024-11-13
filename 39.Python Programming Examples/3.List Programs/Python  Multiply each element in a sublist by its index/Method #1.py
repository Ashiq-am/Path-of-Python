# Python3 code to demonstrate
# to multiply numbers with position
# and add them to return num

import numpy as np

# initialising list
ini_list = [[3, 4, 7], [ 6, 7, 8], [ 10, 7, 5], [ 11, 12, 13]]

# printing initial_list
print ("initial_list ", ini_list)

res = []
# Using Naive Method
for sub_list in ini_list:
	sublistsum = 0

	for i, value in enumerate(sub_list):
		sublistsum = sublistsum + i * value

	res.append(sublistsum)

# printing result
print ("result", res)
