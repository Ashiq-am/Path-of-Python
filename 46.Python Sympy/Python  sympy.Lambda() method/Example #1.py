# import sympy
from sympy import *

# Use sympy.Lambda() method
x = symbols('x')
gfg = Lambda(x, x + 1)

print(gfg(9))
