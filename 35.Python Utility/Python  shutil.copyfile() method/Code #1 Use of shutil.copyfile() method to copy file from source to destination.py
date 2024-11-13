# Python program to explain shutil.copyfile() method

# importing os module
import os

# importing shutil module
import shutil

# path
path = '/home/User/Documents'

# List files and directories
# in '/home/User/Documents'
print("Before copying file:")
print(os.listdir(path))

# Source path
source = "/home/User/Documents/file.txt"

# Destination path
destination = "/home/User/Documents/file(copy).txt"

# Copy the content of
# source to destination
dest = shutil.copyfile(source, destination)

# List files and directories
# in "/home / User / Documents"
print("After copying file:")
print(os.listdir(path))

# Print path of newly
# created file
print("Destination path:", dest)
