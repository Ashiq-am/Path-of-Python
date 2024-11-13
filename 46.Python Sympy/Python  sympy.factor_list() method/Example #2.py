# import sympy
from sympy import *


x = symbols('x')
expr = (x ** 2 - 2 * x + 1)

print("Mathematical expression : {}".format(expr))

# Use sympy.factor_list() method
f = factor_list(expr)

print("List of factors : {}".format(f))
