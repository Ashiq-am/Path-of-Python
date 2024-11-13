# Python program to explain time.mktime() method

# importing time module
import time

# Get the current time
# expressed in seconds
# since the epoch using
# time.time() method
curr_time = time.time()

# Print the value
# returned by time.time() method
print("Current time (in seconds since the epoch):", curr_time)

# Convert the time expressed in seconds
# since the epoch to
# a time.struct_time object
# in local time using
# time.localtime() method
obj = time.localtime(curr_time)

# Print the time.struct_time object
print("\ntime.struct_time object:")
print(obj, "\n")

# Convert the time.struct_time object
# back to the time expressed
# in seconds since the epoch
# in local time using
# time.mktime() method
time_sec = time.mktime(obj)

# Print the time
print("Time (in seconds since the epoch):", time_sec)
