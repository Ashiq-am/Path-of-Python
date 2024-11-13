# Import sympy and ExGaussian
from sympy.stats import ExGaussian, density
from sympy import Symbol

mean = Symbol("mean", integer = True, positive = True)
std = Symbol("std", integer = True, positive = True)
rate = Symbol("rate", integer = True, positive = True)
z = Symbol("z")

# Using sympy.stats.ExGaussian() method
X = ExGaussian("x", mean, std, rate)
gfg = density(X)(z)

print(gfg)
