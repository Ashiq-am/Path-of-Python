# Python program to explain time.asctime() method

# importing time module
import time


# A tuple with 9 attributes
# represnting a time
t = (2019, 8, 22, 11, 21, 48, 3, 234, 0 )

# Convert the tuple
# to a string of the
# form 'Day Mon Date Hour:Min:Sec Year'
# using time.asctime() method
time_str = time.asctime(t)

# Print the string
print(time_str)
