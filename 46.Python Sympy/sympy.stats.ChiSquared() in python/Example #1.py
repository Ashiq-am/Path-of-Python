# Import sympy and chisquared
from sympy.stats import ChiSquared, density
from sympy import Symbol

k = Symbol("k", integer = True, positive = True)
z = Symbol("z")

# Using sympy.stats.ChiSquared() method
X = ChiSquared("x", k)
gfg = density(X)(z)

pprint(gfg)
