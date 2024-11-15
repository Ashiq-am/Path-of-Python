# import sympy
from sympy import *


x, y, z = symbols('x y z')
gfg_exp = 1 / x + (3 * x / 2 - 2)/(x - 4)

# Using sympy.apart() method
gfg_exp = apart(gfg_exp)

print(gfg_exp)
