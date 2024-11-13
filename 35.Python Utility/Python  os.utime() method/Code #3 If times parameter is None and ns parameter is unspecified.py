# Python program to explain os.utime() method

# importing os module
import os

# Path
path = '/home / ihritik / Documents / file.txt'

# Print current access and modification time
# of the above specified path
print("Current access time (in seconds):", os.stat(path).st_atime)
print("Current modification time (in seconds):", os.stat(path).st_mtime)

# Set the access time and
# modification time in nanoseconds
# for the above specified path
# using os.utime() method
os.utime(path)

print("\nAccess and modification time changed\n")

# Print current access and modification time
print("Current access time (in seconds):", os.stat(path).st_atime)
print("Current modification time (in seconds):", os.stat(path).st_mtime)

# If times is None and ns is unspecified,
# then it will be equivalent to
# specifying ns = (atime_ns, mtime_ns)
# where member atime_ns and mtime_ns
# are current time in nanoseconds
