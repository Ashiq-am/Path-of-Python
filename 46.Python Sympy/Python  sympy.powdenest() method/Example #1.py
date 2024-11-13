# import sympy
from sympy import *

x, a, b = symbols('x a b')
expr = (x ** a) ** b

print("Before Conversion : {}".format(expr))

# Use sympy.powdenest() method
smpl = powdenest(expr, force=true)

print("After Conversion : {}".format(smpl))
