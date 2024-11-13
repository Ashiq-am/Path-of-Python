# import inverse_fourier_transform
from sympy import inverse_fourier_transform, exp, sqrt, pi
from sympy.abc import x, k

# Using inverse_fourier_transform()
gfg = inverse_fourier_transform(sqrt(pi)*exp(-(pi * k)**2), k, 4)

print(gfg)
