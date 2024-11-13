# import sympy
from sympy import *

x = symbols('x')

# Use sympy.is_algebraic method
gfg = simplify(2 * x).is_algebraic

print(gfg)
