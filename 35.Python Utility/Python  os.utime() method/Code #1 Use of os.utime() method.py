# Python program to explain os.utime() method

# importing os module
import os

# Path
path = '/home / ihritik / Documents / file.txt'

# Print current access and modification time
# of the above specified path
print("Current access time:", os.stat(path).st_atime)
print("Current modification time:", os.stat(path).st_mtime)

# Access time in seconds
atime = 200000000

# Modification time in seconds
mtime = 100000000

# Set the access time and
# modification time for the
# above specified path
# using os.utime() method
tup = (atime, mtime)
os.utime(path, tup)

print("\nAccess and modification time changed\n")

# Print current access and modification time
print("Current access time:", os.stat(path).st_atime)
print("Current modification time:", os.stat(path).st_mtime)

# Either we can specify times
# or specify ns parameter.
# It is an error to specify
# tuples for both times and ns
