# import sympy
from sympy import *


n = 5
k = symbols('x')
print("Value of n = {} and k = {}".format(n, k))

# Use sympy.bell() method
nth_bell_poly = bell(n, k)

print("The nth bell polynomial : {}".format(nth_bell_poly))
