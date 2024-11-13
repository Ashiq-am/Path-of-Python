# import sympy
from sympy import *

x, y = symbols('x y')

# Use sympy.series() method
gfg = tan(x).series()

print(gfg)
