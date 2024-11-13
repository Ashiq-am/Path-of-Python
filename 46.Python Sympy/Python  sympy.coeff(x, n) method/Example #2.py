# import sympy
from sympy import *


x, y, z = symbols('x y z')
gfg_exp = z * x + x - 3 + 2 * x**2 - y * x**2 + y**3

# Using sympy.coeff(x, n) method
gfg_exp = gfg_exp.coeff(y, 1)

print(gfg_exp)
