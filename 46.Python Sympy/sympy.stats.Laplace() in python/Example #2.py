# Import sympy and Laplace
from sympy.stats import Laplace, density
from sympy import Symbol, pprint

z = 0.6
mu = 2
b = 2.5

# Using sympy.stats.Laplace() method
X = Laplace("x", mu, b)
gfg = density(X)(z)

pprint(gfg)
