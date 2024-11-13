# import sympy
from sympy import *

x, y = symbols('x y')

# Use sympy.is_constant() method
gfg = simplify(sin(x)).is_constant()

print(gfg)
