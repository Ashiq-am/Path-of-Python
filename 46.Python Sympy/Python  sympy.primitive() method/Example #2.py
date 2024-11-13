# import sympy
from sympy import *

x, y = symbols('x y')

# Using sympy.primitive() method
gfg = (2 * x / 7 + 4 * y / 14).primitive()

print(gfg)
