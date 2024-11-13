# Python program to explain os.path.getctime() method

# importing os, time and sys module
import os
import sys
import time

# Path
path = '/home/User/Documents/file2.txt'

# Get the ctime
# for the specified path
try:
    c_time = os.path.getctime(path)
    print("ctime since the epoch:", c_time)

except OSError:
    print("Path '%s' does not exists or is inaccessible" % path)
    sys.exit()

# convert ctime in
# seconds since epoch
# to local time
local_time = time.ctime(c_time)
print("ctime(Local time):", local_time)

# above code will print
# path does not exists or is inaccessible'
# if the specified path does not
# exists or is inaccessible

