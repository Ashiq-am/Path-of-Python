# Python program to explain time.time_ns() method

# importing time module
import time

# Get the epoch
obj = time.gmtime(0)
epoch = time.asctime(obj)
print("epoch is:", epoch)

# Get the time in seconds
# since the epoch
# using time.time() method
time_sec = time.time()

# Get the time in nanoseconds
# since the epoch
# using time.time_ns() method
time_nanosec = time.time_ns()

# Print the time
# in seconds since the epoch
print("Time in seconds since the epoch:", time_sec)

# Print the time
# in nanoseconds since the epoch
print("Time in nanoseconds since the epoch:", time_nanosec)
