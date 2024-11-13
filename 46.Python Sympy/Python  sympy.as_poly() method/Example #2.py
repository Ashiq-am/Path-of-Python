# import sympy
from sympy import *

# Use sympy.as_poly() method
x = symbols('x')
gfg = (x + 5 * x + 6).as_poly()

print(gfg)
