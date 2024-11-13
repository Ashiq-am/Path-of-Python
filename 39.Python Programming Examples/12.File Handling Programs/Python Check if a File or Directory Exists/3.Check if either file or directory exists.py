# Python program to explain os.path.exists() method

# importing os module
import os

# Path
path = 'D:/Pycharm projects/GeeksforGeeks/Nikhil/test_nikhil.txt'

# Check whether the
# specified path is
# an existing file
isExist = os.path.exists(path)
print(isExist)

# Path
path = 'D:/Pycharm projects/GeeksforGeeks/Nikhil/'

# Check whether the
# specified path is
# an existing file
isExist = os.path.exists(path)
print(isExist)
