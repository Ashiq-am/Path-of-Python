# Python program to explain os.remove() method

# importing os module
import os

# path
path = '/home/User/Documents/ihritik'

# Remove the specified
# file path
try:
    os.remove(path)
    print("% s removed successfully" % path)
except OSError as error:
    print(error)
    print("File path can not be removed")
