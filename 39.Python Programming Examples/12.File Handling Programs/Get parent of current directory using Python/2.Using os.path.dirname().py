# Python program to get parent
# directory


import os

# get current directory
path = os.getcwd()
print("Current Directory", path)
print()

# parent directory
parent = os.path.dirname(path)
print("Parent directory", parent)
