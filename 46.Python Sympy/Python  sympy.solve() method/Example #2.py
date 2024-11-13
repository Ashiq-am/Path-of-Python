# import sympy
from sympy import *

x, y = symbols('x y')
gfg_exp = x**2 + 36

print("Before Integration : {}".format(gfg_exp))

# Use sympy.integrate() method
intr = solve(gfg_exp, x)

print("After Integration : {}".format(intr))
