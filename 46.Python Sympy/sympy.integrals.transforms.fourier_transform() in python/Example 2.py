# import fourier_transform
from sympy import fourier_transform, exp
from sympy.abc import x, k

# Using fourier_transform() method
gfg = fourier_transform(exp(-x**2), x, 4)

print(gfg)
