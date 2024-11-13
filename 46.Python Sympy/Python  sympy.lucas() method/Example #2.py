# import sympy
from sympy import *

n = 10
print("Value of n = {}".format(n))

# Use sympy.lucas() method
n_lucas = [lucas(x) for x in range(11)]

print("N lucas number are : {}".format(n_lucas))
