# import sympy
from sympy import *


x, y = symbols('x y')

# Use sympy.Mul() method
mul = Mul(x, y) + Mul(x, x)

print(mul)
