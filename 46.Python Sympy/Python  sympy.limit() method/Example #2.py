# import sympy
from sympy import *

x = symbols('x')
expr = sin(3 * x) / x

print("Expression : {}".format(expr))

# Use sympy.limit() method
limit_expr = limit(expr, x, 0)

print("Limit of the expression tends to 0 : {}".format(limit_expr))
