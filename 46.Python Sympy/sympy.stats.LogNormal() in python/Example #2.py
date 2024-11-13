# Import sympy and LogNormal
from sympy.stats import LogNormal, density
from sympy import Symbol, pprint

z = 2.1
mean = 7.6
std = 4

# Using sympy.stats.LogNormal() method
X = LogNormal("x", mean, std)
gfg = density(X)(z)

pprint(gfg)
