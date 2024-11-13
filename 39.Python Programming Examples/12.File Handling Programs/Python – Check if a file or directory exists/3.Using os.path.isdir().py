# Python program to explain os.path.isdir() method

# importing os.path module
import os.path

# Path
path = '/home/User/Documents/file.txt'

# Check whether the
# specified path is an
# existing directory or not
isdir = os.path.isdir(path)
print(isdir)

# Path
path = '/home/User/Documents/'

# Check whether the
# specified path is an
# existing directory or not
isdir = os.path.isdir(path)
print(isdir)
