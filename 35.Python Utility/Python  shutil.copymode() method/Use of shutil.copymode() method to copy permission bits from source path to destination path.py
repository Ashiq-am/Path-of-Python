# Python program to explain shutil.copymode() method

# importing os module
import os

# importing shutil module
import shutil

# Source file path
src = "/home/ihritik/Desktop/sam3.pl"

# Destination file path
dest = "/home/ihritik/Desktop/encry.py"

# Print the permission bits
# of source and destination path

# As we know, st_mode attribute
# of ‘stat_result’ object returned
# by os.stat() method is an integer
# which represents file type and
# file mode bits (permissions)
# So, here integere is converted into octal form
# to get typical octal permissions.
# Last 3 digit represnts the permission bits
# and rest digits represents the file type
print("Before using shutil.copymode() method:")
print("Permission bits of source:", oct(os.stat(src).st_mode)[-3:])
print("Permission bits of destination:", oct(os.stat(dest).st_mode)[-3:])

# Copy the permission bits
# from source to destination
shutil.copymode(src, dest)

# Print the permission bits
# of destination path
print("\nAfter using shutil.copymode() method:")
print("Permission bits of destination:", oct(os.stat(dest).st_mode)[-3:])
