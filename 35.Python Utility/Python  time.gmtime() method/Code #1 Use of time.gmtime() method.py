# Python program to explain time.gmtime() method

# importing time module
import time


# If secs parameter
# is not given then
# the current time
# as returned by time.time() method
# is used

# Convert the current time in seconds
# since the epoch to a
# time.struct_time object in UTC
obj = time.gmtime()

# Print the time.struct.time object
print(obj)
