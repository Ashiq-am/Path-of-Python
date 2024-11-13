# Import sympy and VonMises
from sympy.stats import VonMises, density
from sympy import Symbol, pprint

z = Symbol("z")
mu = Symbol("mu", positive = True)
k = Symbol("k", positive = True)

# Using sympy.stats.VonMises() method
X = VonMises("x", mu, k)
gfg = density(X)(z)

pprint(gfg)
