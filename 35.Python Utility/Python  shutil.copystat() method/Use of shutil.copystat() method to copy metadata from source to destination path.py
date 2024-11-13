# Python program to explain shutil.copystat() method

# importing os module
import os

# importing shutil module
import shutil

# importing time module
import time

# Source file path
src = "/home/ihritik/Desktop/sam3.pl"

# Destination file path
dest = "/home/ihritik/Desktop/encry.py"

# Print the permission bits
# last access time, last modification time
# and flags value of source and dstination files
print("Before using shutil.copystat() method:")
print("Source metadata:")
print("Permission bits:", oct(os.stat(src).st_mode)[-3:])
print("Last access time:", time.ctime(os.stat(src).st_atime))
print("Last modification time:", time.ctime(os.stat(src).st_mtime))
# print("User defined Flags:", os.stat(src).st_flags)

# Note: st_flags attribute is platform dependent
# and is subject to availability

print("\nDestination metadata:")
print("Permission bits:", oct(os.stat(dest).st_mode)[-3:])
print("Last access time:", time.ctime(os.stat(dest).st_atime))
print("Last modification time:", time.ctime(os.stat(dest).st_mtime))
# print("User defined Flags:", os.stat(dest).st_flags)


# Copy the permission bits
# last access time, last modification time
# and flags value from source to dstination
shutil.copystat(src, dest)

# Print the permission bits
# last access time, last modification time
# and flags value of dstination
print("\nAfter using shutil.copystat() method:")
print("Destination metadata:")
print("Permission bits:", oct(os.stat(dest).st_mode)[-3:])
print("Last access time:", time.ctime(os.stat(dest).st_atime))
print("Last modification time:", time.ctime(os.stat(dest).st_mtime))
# print("User defined Flags:", os.stat(dest).st_flags)

print("Permission bits, last access time and last modification time\n\
copied from source to destination successfully")
