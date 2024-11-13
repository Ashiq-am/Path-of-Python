# Python program to explain PurePath.is_absolute() method

# Import PurePath class from pathlib module
from pathlib import PurePath

# Path
path = '/usr / local / bin'

# Instantiate the PurePath class
obj = PurePath(path)

# Check whether the given path is
# absolute or not
isAbs = obj.is_absolute()

print(isAbs)
