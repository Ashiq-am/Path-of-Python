# Python program to explain os.path.isdir() method

# importing os.path module
import os.path

# Path
path = 'D:/Pycharm projects/GeeksforGeeks/Nikhil/test_nikhil.txt'

# Check whether the
# specified path is an
# existing directory or not
isdir = os.path.isdir(path)
print(isdir)

# Path
path = 'D:/Pycharm projects/GeeksforGeeks/Nikhil/'

# Check whether the
# specified path is an
# existing directory or not
isdir = os.path.isdir(path)
print(isdir)
