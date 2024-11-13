# Python program to explain os.remove() method

# importing os module
import os

# Path
from docutils.utils.math.math2html import file

path = "/home/User/Documents/ihritik"

# Remove the specified
# file path
os.remove(path)
print("% s has been removed successfully" % file)

# if the specified path
# is a directory then
# 'IsADirectoryError' error
# will raised

# Similarly if the specified
# file path does not exists or
# is invalid then corresponding
# OSError will be raised
