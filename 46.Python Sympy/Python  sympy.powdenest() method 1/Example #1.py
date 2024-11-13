# import sympy
from sympy import *

x, y = symbols('x y')
gfg_exp = (x**2)**3

# Use sympy.powdenest() method
fact = powdenest(gfg_exp)

print(fact)
