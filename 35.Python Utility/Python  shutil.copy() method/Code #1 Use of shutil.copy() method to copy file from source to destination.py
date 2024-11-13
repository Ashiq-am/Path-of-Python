# Python program to explain shutil.copy() method

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

# Print file permission
# of the source
perm = os.stat(source).st_mode
print("File Permission mode:", perm, "\n")

# Destination path
destination = "/home/User/Documents/file(copy).txt"

# Copy the content of
# source to destination
dest = shutil.copy(source, destination)

# List files and directories
# in "/home / User / Documents"
print("After copying file:")
print(os.listdir(path))

# Print file permission
# of the destination
perm = os.stat(destination).st_mode
print("File Permission mode:", perm)

# Print path of newly
# created file
print("Destination path:", dest)
