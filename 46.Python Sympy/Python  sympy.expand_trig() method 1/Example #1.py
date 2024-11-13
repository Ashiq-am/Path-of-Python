# Import sympy
from sympy import *

# Define symbols and trigo expression
x, y = symbols('x y')
expn = sin(2 * x) + cos(2 * x)

# Use sympy.expand_trig(expn) method
gfg = expand_trig(expn)

print(gfg)
