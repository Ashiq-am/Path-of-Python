# Import sympy
from sympy import *

# Define symbols and trigo expression
x, y = symbols('x y')
expn = "x**2 + 3 * x - 1 / 2"

# Use sympy.sympify() method
gfg = sympify(expn)

print(gfg)
