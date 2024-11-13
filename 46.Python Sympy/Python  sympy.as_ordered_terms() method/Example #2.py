# import sympy
from sympy import *

x, y = symbols('x y')

# Use sympy.as_ordered_terms() method
gfg = (y + x).as_ordered_terms()

print(gfg)
