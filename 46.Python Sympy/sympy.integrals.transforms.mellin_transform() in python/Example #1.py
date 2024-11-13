# import mellin_transform
from sympy.integrals.transforms import mellin_transform
from sympy import exp
from sympy.abc import x, s

# Using mellin_transform() method
gfg = mellin_transform(exp(-x), x, s)

print(gfg)
