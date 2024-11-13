# Import sympy and Logistic
from sympy.stats import Logistic, density
from sympy import Symbol, pprint

z = Symbol("z")
mu = Symbol("mu", positive = True)
s = Symbol("s", positive = True)

# Using sympy.stats.Logistic() method
X = Logistic("x", mu, s)
gfg = density(X)(z)

pprint(gfg)
