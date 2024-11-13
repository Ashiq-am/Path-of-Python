# import sympy
from sympy import *

x, y = symbols('x y')
gfg_exp = x**2 + 2 * x*y + y**2

# Use sympy.expand_power_base() method
fact = expand_power_base(gfg_exp)

print(fact)
