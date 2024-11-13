# import sympy
from sympy import *
from sympy.abc import a, b

x, y, z = symbols('x y z')
gfg_exp = x**(a + b)

# Use sympy.expand_power_exp() method
fact = expand_power_exp(gfg_exp)

print(fact)
