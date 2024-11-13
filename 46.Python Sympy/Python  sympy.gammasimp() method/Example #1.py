# import sympy
from sympy import *

x = symbols('x')
expr = gamma(x) * gamma(1 - x)
print("Expression = {}".format(expr))

# Use sympy.gammasimp() method
simple_expr = gammasimp(expr)

print("Simplified Expression : {}".format(simple_expr))
