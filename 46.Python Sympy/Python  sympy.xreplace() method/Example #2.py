# import sympy
from sympy import *

x, y = symbols('x y')

f = log(sin(x)) + tan(cos(2 * x))
# Use sympy.xreplace() method
gfg = f.xreplace({x: 2 * y})

print(gfg)
