# import sympy
from sympy import *

x = symbols('x')
expr = gamma(x + 1) / gamma(x - 1)
print("Expression = {}".format(expr))

# Use sympy.gammasimp() method
simple_expr = gammasimp(expr)

print("Simplified Expression : {}".format(simple_expr))
