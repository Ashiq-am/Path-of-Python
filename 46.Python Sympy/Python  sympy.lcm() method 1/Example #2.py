# import sympy
from sympy import *
from sympy.abc import y, x

f = x * y / 2 + y**2
g = 3 * x + 6 * y

# Using sympy.lcm() method
gfg = lcm(f, g)

print(gfg)
