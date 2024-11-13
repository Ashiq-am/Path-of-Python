# import sympy
from sympy import *

x, y = symbols('x y')

# Use sympy.as_independent(variable) method
gfg = (1 + 2 * x + 1 / x).as_independent(x)

print(gfg)
