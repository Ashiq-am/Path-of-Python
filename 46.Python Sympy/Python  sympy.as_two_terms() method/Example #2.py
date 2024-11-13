# import sympy
from sympy import *

x, y = symbols('x y')

# Using sympy.as_two_terms() method
gfg = (x**2 + 4).as_two_terms()

print(gfg)
