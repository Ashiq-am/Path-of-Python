# import sympy
from sympy import *

x = symbols('x')
expr = tan(x)
print("Expression = {}".format(expr))

# Use sympy.rewrite() method
expr_in_terms_of_sin = expr.rewrite(sin)

print("Expression in terms of sin() : {}".format(expr_in_terms_of_sin))
