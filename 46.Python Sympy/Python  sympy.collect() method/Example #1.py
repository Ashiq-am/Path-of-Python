# import sympy
from sympy import *

x, y, z = symbols('x y z')
gfg_exp = x * y + x - 3 + 2 * x**2 - z * x**2 + x**3

# Using sympy.collect() method
gfg_exp = collect(gfg_exp, x)

print(gfg_exp)
