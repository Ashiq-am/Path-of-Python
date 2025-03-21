# import sympy
from sympy import *

x, y, z = symbols('x y z')
gfg_exp = (x**2 + 2 * x + 1)/(x**2 + x)

# Using sympy.apart() method
gfg_exp = apart(gfg_exp)

print(gfg_exp)
