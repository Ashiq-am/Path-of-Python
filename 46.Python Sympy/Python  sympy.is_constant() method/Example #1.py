# import sympy
from sympy import *

x, y = symbols('x y')

# Use sympy.is_constant() method
gfg = simplify(2).is_constant()

print(gfg)
