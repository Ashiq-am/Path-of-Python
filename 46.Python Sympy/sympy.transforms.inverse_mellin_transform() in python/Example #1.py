# import inverse_mellin_transform
from sympy.integrals.transforms import inverse_mellin_transform
from sympy import oo, gamma
from sympy.abc import x, s

# Using inverse_mellin_transform() method
gfg = inverse_mellin_transform(gamma(s), s, x, (0, oo))

print(gfg)
