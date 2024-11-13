# import packages
from sympy.abc import *
from sympy import pi

# finding the circumference of a circle
expression = 2*pi*r

# evaluating the expression
print(expression.evalf(10,subs={r:2}))
