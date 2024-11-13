# import packages
from sympy.abc import *

# creating an expression
expression = 2**x - 4*y + z

# substituting values in the expression
print(expression.subs([(x, 4), (y, 2), (z, 1)]))
