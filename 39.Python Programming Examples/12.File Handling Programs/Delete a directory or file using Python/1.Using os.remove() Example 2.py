# Python program to explain os.remove() method

# importing os module
import os

# Directory name
dir = "Nikhil"

# Path
location = "D:/Pycharm projects/GeeksforGeeks/Authors/"
path = os.path.join(location, dir)

# Remove the specified
# file path
os.remove(path)
print("% s has been removed successfully" % dir)

# if the specified path
# is a directory then
# 'IsADirectoryError' error
# will raised

# Similarly if the specified
# file path does not exists or
# is invalid then corresponding
# OSError will be raised
