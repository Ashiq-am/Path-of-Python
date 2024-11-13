# import sympy
from sympy import *

x = symbols('x')
expr = sin(x) ** 4 - 2 * cos(x) ** 2 * sin(x) ** 2 + cos(x) ** 4

print("Before Simplification : {}".format(expr))

# Use sympy.trigsimp() method
smpl = trigsimp(expr)

print("After Simplification : {}".format(smpl))
