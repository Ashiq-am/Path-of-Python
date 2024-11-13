# Python program to explain time.asctime() method

# importing time module
import time


# If the parameter 't'
# in time.asctime() method
# is not provided then
# the current time as
# returned by time.localtime()
# method is used

# Convert the current time
# as returned by time.localtime() method
# to a string of the
# form 'Day Mon Date Hour:Min:Sec Year'
# using time.asctime() method
time_str = time.asctime()

# Print the string
print(time_str)
