# import sympy
from sympy import *

x = 7
k = 5
print("Value of x = {} and k = {}".format(x, k))

# Use sympy.rf() method
rf_x_k = rf(x, k)

print("Rising factorial rf(x, k) : {}".format(rf_x_k))
