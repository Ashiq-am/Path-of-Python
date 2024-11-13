# import sympy
from sympy import *

x, y = symbols('x y')

# Use sympy.as_ordered_terms() method
gfg = (x ** 2 + 2 * x * y + y ** 2).as_ordered_terms()

print(gfg)
