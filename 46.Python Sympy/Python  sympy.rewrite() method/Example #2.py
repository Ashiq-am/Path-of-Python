# import sympy
from sympy import *

x = symbols('x')
expr = factorial(x)
print("Expression = {}".format(expr))

# Use sympy.rewrite() method
expr_in_terms_of_gamma = expr.rewrite(gamma)

print("Expression in terms of gamma() : {}".format(expr_in_terms_of_gamma))
