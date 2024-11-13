# Python program to explain os.rmdir() method

# importing os module
import os

# Directory name
directory = "GeeksforGeeks"

# Parent Directory
parent = "D:/Pycharm projects/"

# Path
path = os.path.join(parent, directory)

# Remove the Directory
# "GeeksforGeeks"
try:
	os.rmdir(path)
	print("Directory '% s' has been removed successfully" % directory)
except OSError as error:
	print(error)
	print("Directory '% s' can not be removed" % directory)

# if the specified path
# is not an empty directory
# then permission error will
# be raised

# similarly if specified path
# is invalid or is not a
# directory then corresponding
# OSError will be raised
