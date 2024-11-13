# import sympy
from sympy import *

x, y = symbols('x y')

# Use sympy.as_independent(variable) method
gfg = (1 / y ** 2 + x).as_independent(y)

print(gfg)
