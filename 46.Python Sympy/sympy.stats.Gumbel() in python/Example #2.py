# Import sympy and gumbel
from sympy.stats import Gumbel, density
from sympy import Symbol, pprint

z = 0.4
mu = 2
beta = 4

# Using sympy.stats.Gumbel() method
X = Gumbel("x", beta, mu)
gfg = density(X)(z)

pprint(gfg)
