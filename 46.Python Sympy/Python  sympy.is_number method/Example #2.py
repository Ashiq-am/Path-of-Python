# import sympy
from sympy import *

x, y = symbols('x y')

# Use sympy.is_number method
gfg = sin(x).is_number

print(gfg)
