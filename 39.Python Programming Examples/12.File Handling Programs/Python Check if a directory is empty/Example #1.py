# Python program to check whether
# the directory empty or not


import os

# path of the directory
path = "D:/Pycharm projects/GeeksforGeeks/Nikhil"

# Getting the list of directories
dir = os.listdir(path)

# Checking if the list is empty or not
if len(dir) == 0:
	print("Empty directory")
else:
	print("Not empty directory")
