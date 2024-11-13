# import sympy
from sympy import *

x, y, z = symbols('x y z')

# Use sympy.has() method
gfg = (3 * x + 2 * tan(y + I * pi) + log(2 * x)).has(x)

print(gfg)
