# import sympy
from sympy import *

x, y, z, a, b = symbols('x y z a b')
gfg_exp = (x**(a + b))**2

# Use sympy.powdenest() method
fact = powdenest(gfg_exp)

print(fact)
