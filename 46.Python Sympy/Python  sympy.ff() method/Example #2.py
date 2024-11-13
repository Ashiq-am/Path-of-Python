# import sympy
from sympy import *


x = 7
k = 5
print("Value of x = {} and k = {}".format(x, k))

# Use sympy.ff() method
ff_x_k = ff(x, k)

print("Falling factorial ff(x, k) : {}".format(ff_x_k))
