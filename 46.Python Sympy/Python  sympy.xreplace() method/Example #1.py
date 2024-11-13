# import sympy
from sympy import *

x, y = symbols('x y')

f = sin(x) + cos(2 * x)
# Use sympy.xreplace() method
gfg = f.xreplace({2 * x: y})

print(gfg)
