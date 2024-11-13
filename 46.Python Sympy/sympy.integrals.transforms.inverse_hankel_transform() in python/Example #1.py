# import inverse_hankel_transform
from sympy import hankel_transform, inverse_hankel_transform, gamma
from sympy import gamma, exp, sinh, cosh
from sympy.abc import r, k, m, nu, a

ht = hankel_transform(5/(r*m), r, k, nu)

# Using inverse_hankel_transform() method
gfg = inverse_hankel_transform(ht, k, r, nu)

print(gfg)
