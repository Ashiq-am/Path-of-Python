#!/usr/bin/env python3

# importing libraries
import os
import random

# setting up folder name
folder_name = "geeksforgeeks"

# entering into the loop
# to create 2 folder every time this script runs
for i in range(2):

	# generating random number between 0 and 9
	number = int(random.randrange(0, 10))

	print("Creating folder {}".format(number))

	# creating directories
	os.mkdir(folder_name+" {}".format(number))
