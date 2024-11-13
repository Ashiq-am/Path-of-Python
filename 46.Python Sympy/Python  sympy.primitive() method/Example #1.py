# import sympy
from sympy import *

x, y = symbols('x y')

# Using sympy.primitive() method
gfg = (3 * x + 9 * y).primitive()

print(gfg)
