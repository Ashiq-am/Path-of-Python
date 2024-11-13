# import sympy
from sympy import *

x, y = symbols('x y')

f = sin(x) + cos(2 * x)

# Use sympy.replace() method
gfg = f.replace(cos, sin)

print(gfg)
