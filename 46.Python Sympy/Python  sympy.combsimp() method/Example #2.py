# import sympy
from sympy import *

n, k = symbols('n k', integer=True)
expr = binomial(n + 1, k + 1) / binomial(n, k)
print("Expression = {}".format(expr))

# Use sympy.combsimp() method
simple_expr = combsimp(expr)

print("Simplified Expression : {}".format(simple_expr))
