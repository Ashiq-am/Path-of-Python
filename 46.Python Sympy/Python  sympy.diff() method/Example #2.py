# import sympy
from sympy import *

x, y = symbols('x y')
gfg_exp = sin(x)*cos(x)

print("Before Differentiation : {}".format(gfg_exp))

# Use sympy.diff() method
dif = diff(gfg_exp, x)

print("After Differentiation : {}".format(dif))
