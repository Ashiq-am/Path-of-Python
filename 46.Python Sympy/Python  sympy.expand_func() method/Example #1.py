# import sympy
from sympy import *

x = symbols('x')
expr = gamma(x + 3)
print("Expression = {}".format(expr))

# Use sympy.expand_func() method
expand_expr = expand_func(expr)

print("Expanded Expression : {}".format(expand_expr))
