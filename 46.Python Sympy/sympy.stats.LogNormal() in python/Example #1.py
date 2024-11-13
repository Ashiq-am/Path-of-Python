# Import sympy and LogNormal
from sympy.stats import LogNormal, density
from sympy import Symbol, pprint

z = Symbol("z")
mean = Symbol("mean", positive = True)
std = Symbol("std", positive = True)

# Using sympy.stats.LogNormal() method
X = LogNormal("x", mean, std)
gfg = density(X)(z)

pprint(gfg)
