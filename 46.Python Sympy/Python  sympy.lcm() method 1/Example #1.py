# import sympy
from sympy import *
from sympy.abc import x, y

f = x * y**2 + x**2 * y
g = x**2 * y**2

# Using sympy.lcm() method
gfg = lcm(f, g)

print(gfg)
