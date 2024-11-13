# import sympy
from sympy import *


x, y, z = symbols('x y z')
gfg_exp = x * x + x - 3 + 2 * z**2 - y * x**2 + x**3

# Using sympy.collect() method
gfg_exp = collect(gfg_exp, x)

print(gfg_exp)
