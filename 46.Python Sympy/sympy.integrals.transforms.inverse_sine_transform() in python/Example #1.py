# import inverse_sine_transform
from sympy import inverse_sine_transform, exp, sqrt, gamma, pi
from sympy.abc import x, k, a

# Using inverse_sine_transform() method
gfg = inverse_sine_transform(2**((1-2 * a)/2)*k**(a - 1)*gamma(-a / 2 + 1)/gamma((a + 1)/2), k, x)

print(gfg)
