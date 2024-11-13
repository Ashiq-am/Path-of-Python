# import sympy
from sympy import *

# Use sympy.Lambda() method
x, y = symbols('x y')
gfg = Lambda((x, y), x * y)

print(gfg(9, 5))
