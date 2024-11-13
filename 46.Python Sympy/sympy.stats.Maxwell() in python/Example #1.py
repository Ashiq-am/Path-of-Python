# Import sympy and Maxwell
from sympy.stats import Maxwell, density
from sympy import Symbol, pprint

z = Symbol("z")
a = Symbol("a", positive = True)

# Using sympy.stats.Maxwell() method
X = Maxwell("x", a)
gfg = density(X)(z)

pprint(gfg)
