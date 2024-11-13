# import inverse_cosine_transform
from sympy import inverse_cosine_transform, exp, sqrt, pi
from sympy.abc import x, k, a

# Using inverse_cosine_transform() method
gfg = inverse_cosine_transform(sqrt(2)*a/(sqrt(pi)*(a**2 + k**2)), k, x)

print(gfg)
