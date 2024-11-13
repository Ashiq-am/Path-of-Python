# Python program to explain shutil.move() method

# importing os module
import os

# importing shutil module
import shutil

# path
path = 'C:/Users/Rajnish/Desktop/GeeksforGeeks'

# List files and directories
# in 'C:/Users/Rajnish/Desktop/GeeksforGeeks'
print("Before moving file:")
print(os.listdir(path))

# Source path
source = 'C:/Users/Rajnish/Desktop/GeeksforGeeks/source'

# Destination path
destination = 'C:/Users/Rajnish/Desktop/GeeksforGeeks/destination'

# Move the content of
# source to destination
# using shutil.copytree() as parameter
dest = shutil.move(source, destination, copy_function=shutil.copytree)

# List files and directories
# in "C:/Users / Rajnish / Desktop / GeeksforGeeks"
print("After moving file:")
print(os.listdir(path))

# Print path of newly
# created file
print("Destination path:", dest)
