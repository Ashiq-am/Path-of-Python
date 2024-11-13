# import sympy
from sympy import *

x, y, z = symbols('x y z')

# Use sympy.has() method
gfg = (3 * sin(x) + 2 * tan(y + I * pi)).has(z)

print(gfg)
