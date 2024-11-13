# import sympy
from sympy import *
from sympy.abc import z, y

x = symbols('x')

expr = x ** 2 * z + 4 * x * y * z + 4 * y ** 2 * z

print("Mathematical expression : {}".format(expr))

# Use sympy.factor_list() method
f = factor_list(expr)

print("List of factors : {}".format(f))
