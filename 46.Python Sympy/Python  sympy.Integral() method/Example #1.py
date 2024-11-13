# import sympy
from sympy import *

x, y = symbols('x y')
expr = x ** 2 + 2 * y + y ** 3
print("Expression : {} ".format(expr))

# Use sympy.Integral() method
expr_intg = Integral(expr, x)

print("Integral of expression with respect to x : {}".format(expr_intg))
print("Value of the Integral : {} ".format(expr_intg.doit()))
