# Import sympy
from sympy import *

# Define symbols and trigo expression
x, y = symbols('x y')
expn = sin(2 * x)**2 + cos(2 * x)**2

# Use sympy.expand_trig(expn) method
gfg = expand_trig(expn)

print(gfg)
