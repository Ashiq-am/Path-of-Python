# import sympy
from sympy import *

x, y = symbols('x y')
f = Function('f')

# Use sympy.Function() method
gfg = (f(x) + 2 * tan(y + I * pi) + log(2 * x)).atoms(Function)

print(gfg)
