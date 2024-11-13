# import sympy
from sympy import *

x = symbols('x')

# Use sympy.as_coefficients_dict() method
gfg = x**3 + 21 * x + 12

print(gfg.as_coefficients_dict())
