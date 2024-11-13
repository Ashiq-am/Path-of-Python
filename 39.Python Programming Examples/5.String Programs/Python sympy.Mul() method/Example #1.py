# import sympy
from Tools.scripts.nm2def import symbols
from jinja2.nodes import Mul
from sympy import *
x, y = symbols('x y')

# Use sympy.Mul() method
mul = Mul(x, y)

print(mul)
