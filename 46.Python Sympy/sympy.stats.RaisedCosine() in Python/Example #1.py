# Import sympy and RaisedCosine
from sympy.stats import RaisedCosine, density
from sympy import Symbol, pprint

z = Symbol("z")
mu = Symbol("mu", positive = True)
s = Symbol("s", positive = True)

# Using sympy.stats.RaisedCosine() method
X = RaisedCosine("x", mu, s)
gfg = density(X)(z)

pprint(gfg)
