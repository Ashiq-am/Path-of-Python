# import sympy
from sympy import *

x = symbols('x')
expr = sin(x) ** 2 + cos(x) ** 2

print("Before Simplification : {}".format(expr))

# Use sympy.trigsimp() method
smpl = trigsimp(expr)

print("After Simplification : {}".format(smpl))
