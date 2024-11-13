# import sympy
from sympy import *

x, y, z = symbols('x y z', positive=True)
gfg_exp = 5 * log(x)

# Using sympy.logcombine() method
gfg_exp = logcombine(gfg_exp)

print(gfg_exp)
