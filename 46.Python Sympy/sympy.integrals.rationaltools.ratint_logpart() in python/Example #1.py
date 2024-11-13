# import ratint_logpart
from sympy.integrals.rationaltools import ratint_logpart
from sympy.abc import x
from sympy import Poly

# Using ratint_logpart() method
gfg = ratint_logpart(Poly(1, x, domain='ZZ'),
					Poly(x*2 + x + 1, x, domain='ZZ'), x)

print(gfg)
