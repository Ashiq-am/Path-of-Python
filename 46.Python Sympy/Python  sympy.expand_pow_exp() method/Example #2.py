# import sympy
from sympy import *

x, a, b = symbols('x a b')
expr = x ** (2 * a + 3 * b)

print("Before Expansion : {}".format(expr))

# Use sympy.expand_pow_exp() method
smpl = expand_pow_exp(expr)

print("After Expansion : {}".format(smpl))
