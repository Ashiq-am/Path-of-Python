# import ratint
from sympy.integrals.rationaltools import ratint
from sympy.abc import x

# Using ratint() method
gfg = ratint((x**5 - 2*x**3 + x - 2)/12, x)

print(gfg)
