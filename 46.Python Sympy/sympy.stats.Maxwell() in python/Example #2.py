# Import sympy and Maxwell
from sympy.stats import Maxwell, density
from sympy import Symbol, pprint

z = 1.2
a = 3

# Using sympy.stats.Maxwell() method
X = Maxwell("x", a)
gfg = density(X)(z)

pprint(gfg)
