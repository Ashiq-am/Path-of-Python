# import sympy
from sympy import *

x, a, b = symbols('x a b')
expr = ((x ** (2 * a + b)) * (x ** (-a + b)))

print("Before Simplification : {}".format(expr))

# Use sympy.powsimp() method
smpl = powsimp(expr)

print("After Simplification : {}".format(smpl))
