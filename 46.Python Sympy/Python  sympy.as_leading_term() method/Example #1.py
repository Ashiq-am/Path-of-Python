# import sympy
from sympy import *

x, y = symbols('x y')

# Use sympy.as_leading_term(variable) method
gfg = (x ** 2 + 2 * x * y + y ** 2).as_leading_term(y)

print(gfg)
