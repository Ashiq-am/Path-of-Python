# import laplace_transform
from sympy.integrals import laplace_transform
from sympy.abc import t, s, a

# Using laplace_transform() method
gfg = laplace_transform(t**a, t, s)

print(gfg)
