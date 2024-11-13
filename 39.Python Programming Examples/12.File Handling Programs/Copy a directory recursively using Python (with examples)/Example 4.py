# Python program to demonstrate
# shutil.copytree()


# importing modules
import shutil

# Source path
src = 'D:/Pycharm projects/GeeksforGeeks/src'

# Destination path
dest = 'D:/Pycharm projects/GeeksforGeeks/dst'

# Copying the contents from Source
# to Destination without some
# specified files or directories
shutil.copytree(src, dest, ignore = shutil.ignore_patterns('*.txt', 'a'))
