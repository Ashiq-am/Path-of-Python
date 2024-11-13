# import sympy
from sympy import *
from sympy.abc import x

f = 5 * x**2 + 10 * x + 3
g = 2 * x**2 + 2

# Using sympy.div() method
q, r = div(f, g, domain ='QQ')

print(q)
print(r)
