# Python program to explain os.listdir() method

# importing os module
import os

# Get the path of current working directory
path = os.getcwd()

# Get the list of all files and directories
# in current working directory
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")
# print the list
print(dir_list)
