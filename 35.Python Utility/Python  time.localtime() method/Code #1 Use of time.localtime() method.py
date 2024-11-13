# Python program to explain time.localtime() method

# importing time module
import time

# If secs parameter
# is not given then
# the current time as
# returned by time.time() method
# is used

# Convert the current time in seconds
# since the epoch to a
# time.struct_time object in Local time
obj = time.localtime()

# Print the time.struct.time object
print(obj)

# We can change it to
# Day Mon date Hour:Min:Sec year
# format using time.asctime() method
t = time.asctime(obj)
print(t)
