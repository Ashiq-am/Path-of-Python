# import sympy
from sympy import *

x, y = symbols('x y')

# Using sympy.as_coeff_add() method
gfg = (x**2 + 4 * x + 4).as_coeff_add()

print(gfg)
