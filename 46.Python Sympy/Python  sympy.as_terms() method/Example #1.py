# import sympy
from sympy import *

x, y = symbols('x y')

# Use sympy.as_terms() method
gfg = (x ** 2 + 2 * x * y + y ** 2).as_terms()

print(gfg)
