# import sine_transform
from sympy import sine_transform, exp
from sympy.abc import x, k, a

# Using sine_transform() method
gfg = sine_transform(x * exp(-a * x**2), x, k)

print(gfg)
