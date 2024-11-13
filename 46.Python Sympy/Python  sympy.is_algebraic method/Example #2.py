# import sympy
from sympy import *

# Use sympy.is_algebraic method
gfg = simplify(5 * I).is_algebraic

print(gfg)
