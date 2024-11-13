# import sympy
from sympy import *

x, y = symbols('x y')
gfg_exp = cos(x)

print("Before Integration : {}".format(gfg_exp))

# Use sympy.integrate() method
intr = integrate(gfg_exp, (x, -oo, oo))

print("After Integration : {}".format(intr))
