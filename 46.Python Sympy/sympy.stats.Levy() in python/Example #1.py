# Import sympy and Levy
from sympy.stats import Levy, density
from sympy import Symbol, pprint

z = Symbol("z")
mu = Symbol("mu", positive = True)
c = Symbol("c", positive = True)

# Using sympy.stats.Levy() method
X = Levy("x", mu, c)
gfg = density(X)(z)

pprint(gfg)
