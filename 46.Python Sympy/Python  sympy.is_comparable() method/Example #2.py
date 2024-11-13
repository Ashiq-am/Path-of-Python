# import sympy
from sympy import *

x, y, z = symbols('x y z')

# Use sympy.is_comparable() method
gfg = (pi / 2).is_comparable

print(gfg)
