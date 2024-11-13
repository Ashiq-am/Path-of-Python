# import sympy
from sympy import *

x, y = symbols('x y')
f = Function('f')

# Use sympy.Function() method
gfg = (2 + 3 * cos(y) + 5 * log(2 * x)).atoms(Function)

print(gfg)
