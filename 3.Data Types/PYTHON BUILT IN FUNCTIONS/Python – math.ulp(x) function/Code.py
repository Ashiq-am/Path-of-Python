# python program to explain
# math.ulp(x) for different values of x
import math
import sys

# when x is NaN
x = float('nan')
print(math.ulp(x))

# when x is positive infinity
x = float('inf')
print(math.ulp(x))

# when x is negative infinity
print(math.ulp(-x))

# when x = 0
x = 0.0
print(math.ulp(x))

# when x is maximum representable float
x = sys.float_info.max
print(math.ulp(x))

# x is a positve finite number
x = 5
print(math.ulp(x))

# when x is a negative number
x = -5
print(math.ulp(x))
