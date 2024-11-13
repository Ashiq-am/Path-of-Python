# import ratint_logpart
from sympy.integrals.rationaltools import ratint_logpart
from sympy.abc import x, y
from sympy import Poly

# Using ratint_logpart() method
gfg = ratint_logpart(Poly(10, y, domain='ZZ'),
			Poly(y**2 - 3*y - 2, y, domain='ZZ'), y)

print(gfg)
