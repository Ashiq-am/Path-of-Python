# import sympy
from sympy import *

n = symbols('n', integer=True)
expr = factorial(n) / factorial(n - 3)
print("Expression = {}".format(expr))

# Use sympy.combsimp() method
simple_expr = combsimp(expr)

print("Simplified Expression : {}".format(simple_expr))
