# import inverse_hankel_transform
from sympy import hankel_transform, inverse_hankel_transform, gamma
from sympy import gamma, exp, sinh, cosh
from sympy.abc import r, k, m, nu, a

ht = hankel_transform(exp(-2*r), r, k, 0)

# Using inverse_hankel_transform() method
gfg = inverse_hankel_transform(ht, k, r, 0)

print(gfg)
