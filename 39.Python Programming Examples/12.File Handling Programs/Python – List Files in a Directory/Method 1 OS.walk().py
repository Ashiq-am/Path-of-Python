# import OS module
import os

# This is my path
path="C://Users//Vanshi//Desktop//gfg"

# to store files in a list
list = []

# dirs=directories
for (root, dirs, file) in os.walk(path):
	for f in file:
		if '.txt' in f:
			print(f)
