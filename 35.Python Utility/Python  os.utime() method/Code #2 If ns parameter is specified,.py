# Python program to explain os.utime() method

# importing os module
import os

# Path
path = '/home / ihritik / Documents / file.txt'

# Print current access and modification time
# of the above specified path
print("Current access time (in seconds):", os.stat(path).st_atime)
print("Current modification time (in seconds):", os.stat(path).st_mtime)

# Access time in nanoseconds
atime_ns = 20000000012345

# Modification time in nanoseconds
mtime_ns = 10000000012345

# Set the access time and
# modification time in nanoseconds
# for the above specified path
# using os.utime() method
# (ns is keyword only argument)
tup = (atime_ns, mtime_ns)
os.utime(path, ns=tup)

print("\nAccess and modification time changed\n")

# Print current access and modification time
print("Current access time (in seconds):", os.stat(path).st_atime)
print("Current modification time (in seconds):", os.stat(path).st_mtime)

# Either we can specify times
# or specify ns parameter.
# It is an error to specify
# tuples for both times and ns
