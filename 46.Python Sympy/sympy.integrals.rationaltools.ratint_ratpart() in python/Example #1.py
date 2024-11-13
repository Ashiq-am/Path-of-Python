# import ratint_ratpart
from sympy.integrals.rationaltools import ratint_ratpart
from sympy.abc import x, y
from sympy import Poly

# Using ratint_ratpart() method
gfg = ratint_ratpart(Poly(5, x, domain='ZZ'), Poly(x**4 + 1, x, domain='ZZ'), x)

print(gfg)
