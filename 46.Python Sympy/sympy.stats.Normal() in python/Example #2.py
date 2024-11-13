# Import sympy and Normal
from sympy.stats import Normal, density
from sympy import Symbol, pprint

z = 2
mean = 1.8
std = 4

# Using sympy.stats.Normal() method
X = Normal("x", mean, std)
gfg = density(X)(z)

pprint(gfg)
