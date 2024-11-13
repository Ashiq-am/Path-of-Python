# Import sympy and betanoncentral
from sympy.stats import BetaNoncentral, density
from sympy import Symbol, pprint

alpha = 4
beta = 5
lamda = 1

# Using sympy.stats.BetaNoncentral() method
X = BetaNoncentral("x", alpha, beta, lamda)
gfg = density(X)(2)

pprint(gfg, use_unicode = False)
