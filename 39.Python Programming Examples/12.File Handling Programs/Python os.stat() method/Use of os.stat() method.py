# Python program to explain os.stat() method

# importing os module
import os

# path
path = '/home/User/Documents/file.txt'

# Get the status of
# the specified path
status = os.stat(path)

# Print the status
# of the specified path
print(status)
