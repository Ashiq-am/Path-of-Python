# Import sympy and Normal
from sympy.stats import Normal, density
from sympy import Symbol, pprint

z = Symbol("z")
mean = Symbol("mean", positive = True)
std = Symbol("std", positive = True)

# Using sympy.stats.Normal() method
X = Normal("x", mean, std)
gfg = density(X)(z)

pprint(gfg)
