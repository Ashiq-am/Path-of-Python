# import sympy
from sympy import *

x = symbols('x')
expr = (4 * x ** 3 + 21 * x ** 2 + 10 * x + 12) / (x ** 4 + 5 * x ** 3 + 5 * x ** 2 + 4 * x)

print("Mathematical expression : {}".format(expr))

# Use sympy.apart() method
pd = apart(expr)

print("After Partial Decomposition : {}".format(pd))
