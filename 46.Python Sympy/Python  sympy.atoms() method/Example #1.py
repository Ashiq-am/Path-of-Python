# import sympy
from sympy import *

# Use sympy.atoms() method
x = symbols('x')
gfg = (2 + x + 7 * tan(x + I * pi)).atoms(Number)

print(gfg)
