# Import sympy and Benini
from sympy.stats import Benini, density, cdf
from sympy import Symbol, simplify, pprint

alpha = Symbol("alpha", positive = True)
beta = Symbol("beta", positive = True)
sigma = Symbol("sigma", positive = True)
z = Symbol("z")

# Using sympy.stats.Benini() method
X = Benini("x", alpha, beta, sigma)
GFG = density(X)(z)

pprint(GFG, use_unicode = False)
