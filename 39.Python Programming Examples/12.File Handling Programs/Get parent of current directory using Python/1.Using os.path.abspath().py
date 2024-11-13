# Python program to get parent
# directory


import os

# get current directory
path = os.getcwd()
print("Current Directory", path)

# prints parent directory
print(os.path.abspath(os.path.join(path, os.pardir)))
