# Python program to explain PurePath.name property

# Import PurePath class from pathlib module
from pathlib import PurePath

# Path
path = '/Desktop / file.txt'

# Instantiate the PurePath class
obj = PurePath(path)

# Get the final path component
comp = obj.name

print(comp)
