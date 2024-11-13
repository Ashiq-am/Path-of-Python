# Python program to explain time.mktime() method

# importing time module
import time

# A tuple containing 9 elements
# corresponding to time.struct_time object
# for example: consider the below object
# time.struct_time(tm_year = 2019, tm_mon = 9, tm_mday = 13,
# tm_hour = 1, tm_min = 30, tm_sec = 26, tm_wday = 4,
# tm_yday = 256, tm_isdst = 0)

# Tuple corresponding to above
# time.struct_time object will be
tup = (2019, 9, 13, 1, 30, 26, 4, 256, 0)

# Convert the above specified tuple
# to local time expressed in seconds
# since the epoch
# using time.mktime() method
time_sec = time.mktime(tup)

# Print the time
print("Local Time (in seconds since the epoch):", time_sec)
