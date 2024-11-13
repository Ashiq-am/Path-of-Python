# Python program to explain shutil.copy() method

# importing shutil module
import shutil

# If the source and destination
# represents the same file
# 'SameFileError' exception
# will be raised

# If the destination is
# not writable
# 'PermissionError' exception
# will be raised


# Source path
source = "/home/User/Documents/file.txt"

# Destination path
destination = "/home/User/Documents/file.txt"

# Copy the content of
# source to destination
shutil.copy(source, destintion)
