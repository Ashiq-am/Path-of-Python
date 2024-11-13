# import sympy
from sympy import *

x, y = symbols('x y')

# Use sympy.Mul() method
gfg = Add(Mul(x, y), Mul(x, x))

print(gfg)
