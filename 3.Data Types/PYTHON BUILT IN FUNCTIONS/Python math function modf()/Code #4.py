# Python3 program to demonstrate the
# application of function modf()

# This will import math module
import math

# modf() function to multiply fractional part
a = math.modf(11.2)
b = math.modf(12.3)

# Multiply the fractional part as is stored
# in 0th index of both the tuple
print(a[0]*b[0])
