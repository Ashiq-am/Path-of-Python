# import ratint_ratpart
from sympy.integrals.rationaltools import ratint_ratpart
from sympy.abc import x, y
from sympy import Poly

# Using ratint_ratpart() method
gfg = ratint_ratpart(Poly(13, x, domain='ZZ'), Poly(4*x**2 + x - 2, x, domain='ZZ'), x)

print(gfg)
