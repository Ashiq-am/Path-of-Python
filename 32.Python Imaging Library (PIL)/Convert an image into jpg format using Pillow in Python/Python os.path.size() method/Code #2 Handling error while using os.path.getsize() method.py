# Python program to explain os.path.getsize() method

# importing os module
import os

# Path
import sys

path = '/home/User/Desktop/file2.txt'

# Get the size (in bytes)
# of specified path
try:
    size = os.path.getsize(path)

except OSError:
    print("Path '%s' does not exists or is inaccessible" % path)
    sys.exit()

# Print the size (in bytes)
# of specified path
print("Size (In bytes) of '% s':" % path, size)
