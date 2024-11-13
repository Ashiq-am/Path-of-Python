# import sympy
from sympy import *

x, a, b = symbols('x a b')
expr = x ** a * x ** b

print("Before Simplification : {}".format(expr))

# Use sympy.powsimp() method
smpl = powsimp(expr)

print("After Simplification : {}".format(smpl))
