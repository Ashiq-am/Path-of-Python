# import sympy
from sympy import *

x, y = symbols('x y')

# Using sympy.Mod() method
gfg = Mod(x**2, y).subs({x:7, y:5})

print(gfg)
