# Import sympy and Laplace
from sympy.stats import Laplace, density
from sympy import Symbol, pprint

z = Symbol("z")
mu = Symbol("mu", positive = True)
b = Symbol("b", positive = True)

# Using sympy.stats.Laplace() method
X = Laplace("x", mu, b)
gfg = density(X)(z)

pprint(gfg)
