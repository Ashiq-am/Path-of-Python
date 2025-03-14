# import sympy
from sympy import *

x = symbols('x')

# Use sympy.as_coefficient() method
gfg = x ** 3 + 21 * x ** 2 + 121 * x + 4

print(gfg.as_coefficient(x))
