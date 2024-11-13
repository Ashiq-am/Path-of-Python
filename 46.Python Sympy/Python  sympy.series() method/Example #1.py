# import sympy
from sympy import *

x, y = symbols('x y')

# Use sympy.series() method
gfg = cos(x).series()

print(gfg)
