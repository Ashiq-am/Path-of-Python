# import sympy
from sympy import *

x, y = symbols('x y')

# Use sympy.as_terms() method
gfg = (y + x).as_terms()

print(gfg)
