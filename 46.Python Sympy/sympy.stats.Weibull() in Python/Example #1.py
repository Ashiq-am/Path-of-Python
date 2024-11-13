# Import sympy and Weibull
from sympy.stats import Weibull, density
from sympy import Symbol, pprint

z = Symbol("z")
a = Symbol("a", positive = True)
l = Symbol("l", positive = True)

# Using sympy.stats.Weibull() method
X = Weibull("x", a, l)
gfg = density(X)(z)

pprint(gfg)
