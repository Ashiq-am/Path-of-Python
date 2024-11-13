# Python program to explain os.path.isfile() method

# importing os module
import os

# Path
path = 'C:/Users/gfg/Desktop/file.txt'

# Check whether the
# specified path is
# an existing file
isFile = os.path.isfile(path)
print(isFile)

# Path
path = '/home/User/Desktop/'

# Check whether the
# specified path is
# an existing file
isFile = os.path.isfile(path)
print(isFile)
