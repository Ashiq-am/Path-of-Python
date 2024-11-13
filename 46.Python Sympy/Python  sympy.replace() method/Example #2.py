# import sympy
from sympy import *

x, y = symbols('x y')

f = log(sin(x)) + tan(cos(2 * x))
# Use sympy.replace() method
gfg = f.replace(log, tan)

print(gfg)
