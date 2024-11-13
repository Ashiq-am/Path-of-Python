# import sympy
import sympy
from Tools.scripts.nm2def import symbols
from numpy import diff
from sympy import *

x, y = symbols('x y')
gfg_exp = x + y
exp = sympy.expand(gfg_exp**2)
print("Before Differentiation : {}".format(exp))

# Use sympy.diff() method
dif = diff(exp, x)

print("After Differentiation : {}".format(dif))
