# Python program to explain os.path.getctime() method

# importing os and time module
import os
import time

# Path
path = '/home/User/Documents/file.txt'

# Get the ctime of last
# for the specified path
c_time = os.path.getctime(path)
print("ctime since the epoch:", c_time)

# convert the ctime in
# seconds since epoch
# to local time
local_time = time.ctime(c_time)
print("ctime (Local time):", local_time)
