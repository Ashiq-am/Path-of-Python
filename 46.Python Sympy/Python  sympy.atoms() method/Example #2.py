# import sympy
from sympy import *

# Use sympy.atoms() method
x = symbols('x')
gfg = (2 + x + 7 * log(x + I * pi)).atoms(Number, Symbol, NumberSymbol)

print(gfg)
