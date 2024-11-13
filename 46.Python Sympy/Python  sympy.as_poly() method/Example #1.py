# import sympy
from sympy import *

# Use sympy.as_poly() method
x = symbols('x')
gfg = (x**2 + 4 * x + 16).as_poly()

print(gfg)
