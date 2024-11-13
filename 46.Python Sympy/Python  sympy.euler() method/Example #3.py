# import sympy
from sympy import *


n = 4
k = 3
print("Value of n = {} and k = {}".format(n, k))

# Use sympy.euler() method
nth_euler_poly = euler(n, k)

print("The nth euler polynomial value : {}".format(nth_euler_poly))
