# Import sympy and RaisedCosine
from sympy.stats import RaisedCosine, density
from sympy import Symbol, pprint

z = 1.2
mu = 1
s = 3

# Using sympy.stats.RaisedCosine() method
X = RaisedCosine("x", mu, s)
gfg = density(X)(z)

pprint(gfg)
