# Python program to explain time.gmtime() method

# importing time module
import time


# Time in seconds
# since the epoch
secs = 40000

# Convert the given time in seconds
# since the epoch to a
# time.struct_time object in UTC
# using time.gmtime() method
obj = time.gmtime(secs)

# Print the time.struct_time object
print("time.struct_time object for seconds =", secs)
print(obj)


# Time in seconds
# since the epoch
secs = 40000.7856

# Convert the given time in seconds
# since the epoch to a
# time.struct_time object in UTC
# using time.gmtime() method
obj = time.gmtime(secs)

# Print the time.struct_time object
print("\ntime.struct_time object for seconds =", secs)
print(obj)


# Output for sec = 40000
# and secs = 40000.7856
# will be same beacause
# fractions in 40000.7856
# i.e .7856 will be ignored
