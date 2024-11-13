# import sympy
from sympy import *
from sympy.abc import x

f = (12 * x + 12)*x
g = 32 * x**2

# Using sympy.gcd() method
gfg = gcd(f, g)

print(gfg)
