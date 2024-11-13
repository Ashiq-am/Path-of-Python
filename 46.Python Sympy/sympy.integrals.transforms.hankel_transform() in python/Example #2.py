# import hankel_transform
from sympy import hankel_transform, inverse_hankel_transform
from sympy import gamma, exp, sinh, cosh
from sympy.abc import r, k, m, nu, a

# Using hankel_transform() method
gfg = hankel_transform(1/(r*m)**2, r, k, 3)

print(gfg)
