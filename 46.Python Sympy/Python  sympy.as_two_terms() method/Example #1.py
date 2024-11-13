# import sympy
from sympy import *

x, y = symbols('x y')

# Using sympy.as_two_terms() method
gfg = (3 * x + 5 * y + 6).as_two_terms()

print(gfg)
