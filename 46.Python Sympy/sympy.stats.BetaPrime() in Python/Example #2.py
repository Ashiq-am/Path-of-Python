# Import sympy and betaprime
from sympy.stats import BetaPrime, density
from sympy import Symbol, pprint

alpha = 4
beta = 5
z = Symbol("z")

# Using sympy.stats.BetaPrime() method
X = BetaPrime("x", alpha, beta)
gfg = density(X)(z)

pprint(gfg, use_unicode = False)
