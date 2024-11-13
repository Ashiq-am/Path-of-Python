# import sympy
from sympy import *


x, y, z = symbols('x y z')
gfg_exp = x * y + x - 3 + 2 * x**2 - z * x**2 + x**3

# Using sympy.coeff(x, n) method
gfg_exp = gfg_exp.coeff(x, 2)

print(gfg_exp)
