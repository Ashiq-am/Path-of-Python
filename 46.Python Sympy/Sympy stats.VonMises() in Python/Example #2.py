# Import sympy and VonMises
from sympy.stats import VonMises, density
from sympy import Symbol, pprint

z = 0.78
mu = 1.23
k = 4

# Using sympy.stats.VonMises() method
X = VonMises("x", mu, k)
gfg = density(X)(z)

pprint(gfg)
