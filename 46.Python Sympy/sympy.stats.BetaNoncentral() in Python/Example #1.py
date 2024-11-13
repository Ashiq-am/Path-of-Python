# Import sympy and betanoncentral
from sympy.stats import BetaNoncentral, density
from sympy import Symbol, pprint

alpha = Symbol("alpha", positive = True)
beta = Symbol("beta", positive = True)
lamda = Symbol("lamda", nonnegative = True)
z = Symbol("z")

# Using sympy.stats.BetaNoncentral() method
X = BetaNoncentral("x", alpha, beta, lamda)
gfg = density(X)(z)

pprint(gfg, use_unicode = False)
