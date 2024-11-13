# import sympy
from sympy import *

x, y = symbols('x y')
gfg_exp = tan(x)

print("Before Integration : {}".format(gfg_exp))

# Use sympy.integrate() method
intr = integrate(gfg_exp, (x, -1, 1))

print("After Integration : {}".format(intr))
