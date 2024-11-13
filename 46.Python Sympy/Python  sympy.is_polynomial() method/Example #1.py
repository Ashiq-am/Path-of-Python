# import sympy
from sympy import *

x, y = symbols('x y')

# Use sympy.is_polynomial() method
gfg = simplify(x ** 2 + 2 * y * x + y ** 2).is_polynomial()

print(gfg)
