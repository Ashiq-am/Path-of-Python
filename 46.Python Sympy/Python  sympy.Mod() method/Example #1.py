# import sympy
from sympy import *

x, y = symbols('x y')

# Using sympy.Mod() method
gfg = Mod(x, y).subs({x:7, y:2})

print(gfg)
