# import sympy
from sympy import *

x = symbols('x')
expr = 1 / (x + 3)(x + 2)

print("Mathematical expression : {}".format(expr))

# Use sympy.factor_list() method
pd = apart(expr)

print("After Partial Decomposition : {}".format(pd))
