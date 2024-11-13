# import sympy
from sympy import *

x = symbols('x')
expr = (x ** 3 + x ** 2 - x - 1) / (x ** 2 + 2 * x + 1)

print("Before Simplification : {}".format(expr))

# Use sympy.simplify() method
smpl = simplify(expr)

print("After Simplification : {}".format(smpl))
