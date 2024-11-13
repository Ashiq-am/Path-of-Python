# import sympy
from sympy import *


n = 5
k = 3
print("Value of n = {} and k = {}".format(n, k))

# Use sympy.bell() method
nth_bell_poly = bell(n, k)

print("The nth bell polynomial value : {}".format(nth_bell_poly))
