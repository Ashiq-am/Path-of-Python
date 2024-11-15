# Python program to explain shutil.copy2() method

# importing os module
import os

# importing shutil module
import shutil

# Source path
source = "/home/User/Documents/file.txt"

# Destination path
destination = "/home/User/Desktop/"

# Copy the content of
# source to destination
dest = shutil.copy2(source, destination)

# List files and directories
# in "/home / User / Desktop"
print("After copying file:")
print(os.listdir(destination))

# Print path of newly
# created file
print("Destination path:", dest)
