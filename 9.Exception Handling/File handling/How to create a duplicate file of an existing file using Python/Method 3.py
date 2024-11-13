# Python program to create the duplicate of an already
# existing file
import os
D = r"F:\Dest"
# importing the shutil module
import shutil

print("Before copying file:")
print(os.listdir(D))

# src contains the path of the source file
src=r"C:\Users\YASH\OneDrive\Desktop\small\Src\Test.py"

# dest contains the path of the destination file
dest = r"F:\Dest\Test.py"

# using copy2()
path=shutil.copy2(src,dest)

# A new duplicate file is added at
# the destination with name we mention
# on the path
print("After copying file:")
print(os.listdir(D))

# print path of the newly created duplicate file
print("Path of the duplicate file is:")
print(path)
