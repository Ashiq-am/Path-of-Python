# Import sympy and gumbel
from sympy.stats import Gumbel, density
from sympy import Symbol, pprint

z = Symbol("z")
mu = Symbol("mu")
beta = Symbol("beta", positive = True)

# Using sympy.stats.Gumbel() method
X = Gumbel("x", beta, mu)
gfg = density(X)(z)

pprint(gfg)
