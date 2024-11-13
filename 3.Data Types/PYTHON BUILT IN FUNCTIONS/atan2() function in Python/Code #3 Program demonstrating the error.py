# Python3 program to demonstrate the
# TypeError in atan() method

# importing math
import math

y, x = 3, 6

# when integer values are passed
# it returns a TypeError
theta = math.atan2([y], [x])
print(theta)
