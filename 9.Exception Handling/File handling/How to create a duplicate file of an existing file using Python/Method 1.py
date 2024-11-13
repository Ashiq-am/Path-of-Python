# Python program to create the duplicate of
# an already existing file
import os
D = r"F:\Dest"

# importing the shutil module
import shutil

print("Before copying file:")
print(os.listdir(D))

# src contains the path of the source file
src = r"C:\Users\YASH\OneDrive\Desktop\small\Src\Test.py"

# dest contains the path of the destination file
dest = r"F:\Dest\Test.py"

# create duplicate of the file at the destination,
# with the name mentioned
# at the end of the destination path
# if a file with the same name doesn't already
# exist at the destination,
# a new file with the name mentioned is created
path = shutil.copyfile(src,dest)

print("After copying file:")
print(os.listdir(D))

# print path of the newly created duplicate file
print("Path of the duplicate file is:")
print(path)
