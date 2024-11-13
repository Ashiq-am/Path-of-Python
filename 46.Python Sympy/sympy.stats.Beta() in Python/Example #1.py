# Import sympy and beta
from sympy.stats import Beta, density, E, variance
from sympy import Symbol, simplify, pprint, factor

alpha = Symbol("alpha", positive = True)
beta = Symbol("beta", positive = True)
z = Symbol("z")

# Using sympy.stats.Beta() method
X = Beta("x", alpha, beta)
gfg = density(X)(z)

pprint(gfg, use_unicode = False)
