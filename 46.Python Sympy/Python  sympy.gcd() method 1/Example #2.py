# import sympy
from sympy import *
from sympy.abc import x

f = 3 * x**2 / 2
g = 9 * x / 4

# Using sympy.gcd() method
gfg = gcd(f, g)

print(gfg)
