# import sympy
from sympy import *

x, y = symbols('x y')

# Use sympy.as_leading_term(variable) method
gfg = (x * sin(x) * cos(y) + log(tan(x))).as_leading_term(y)

print(gfg)
