# import ratint
from sympy.integrals.rationaltools import ratint
from sympy.abc import y

# Using ratint() method
gfg = ratint((3*y**3 + 4*x**2 + y - 2), y)

print(gfg)
