# import sympy
from sympy import *


def squared(n):
    return n ** 2


x = symbols('x')
expr = x ** 2

# Use sympy.lambdify() method
f = lambdify(x, expr, {"**": squared})

print("Using lambda function in SymPy to evaluate squared function : {}".format(f(10)))
