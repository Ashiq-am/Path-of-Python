# import sympy
from sympy import *

x, y, z = symbols('x y z', positive=True)
gfg_exp = log(x ** 3)

# Using sympy.expand_log() method
gfg_exp = expand_log(gfg_exp)

print(gfg_exp)
