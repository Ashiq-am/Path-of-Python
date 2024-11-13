# Python program to explain time.localtime() method

# importing time module
import time

# Time in seconds
# since the epoch
secs = 950000000

# Convert the given time in seconds
# since the epoch to a
# time.struct_time object in local time
# using time.localtime() method
obj = time.localtime(secs)

# Print the time.struct_time object
print("time.struct_time object for seconds =", secs)
print(obj)


# Time in seconds
# since the epoch
secs = 950000000.81956

# Convert the given time in seconds
# since the epoch to a
# time.struct_time object in local time
# using time.localtime() method
obj = time.localtime(secs)

# Print the time.struct_time object
print("\ntime.struct_time object for seconds =", secs)
print(obj)


# Output for secs = 950000000
# and secs = 950000000.81956
# will be same beacause
# fractions in 950000000.81956
# i.e .81956 will be ignored
