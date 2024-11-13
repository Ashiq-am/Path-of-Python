# import sympy
from sympy import *

x = symbols('x')
expr = sin(x) ** 2 + cos(x) ** 2

print("Before Simplification : {}".format(expr))

# Use sympy.simplify() method
smpl = simplify(expr)

print("After Simplification : {}".format(smpl))
