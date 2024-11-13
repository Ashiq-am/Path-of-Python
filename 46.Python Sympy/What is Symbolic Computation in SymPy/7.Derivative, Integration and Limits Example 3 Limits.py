from sympy import *

x = Symbol('x')

print(limit(x**2, x, 5))
print(limit(x**3, x, oo))
