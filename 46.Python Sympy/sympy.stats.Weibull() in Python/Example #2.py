# Import sympy and Weibull
from sympy.stats import Weibull, density
from sympy import Symbol, pprint

z = 2
a = 3
l = 4

# Using sympy.stats.Weibull() method
X = Weibull("x", a, l)
gfg = density(X)(z)

pprint(gfg)
