# import sympy
from sympy import *


n = 5
k = symbols('x')
print("Value of n = {} and k = {}".format(n, k))

# Use sympy.euler() method
nth_euler_poly = euler(n, k)

print("The nth euler polynomial : {}".format(nth_euler_poly))
