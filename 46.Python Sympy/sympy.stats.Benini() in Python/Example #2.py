# Import sympy and Benini
from sympy.stats import Benini, density, cdf
from sympy import Symbol, simplify, pprint

alpha = 4
beta = 6
sigma = 3
z = 0.2

# Using sympy.stats.Benini() method
X = Benini("x", alpha, beta, sigma)
GFG = density(X)(z)

pprint(GFG, use_unicode = False)
