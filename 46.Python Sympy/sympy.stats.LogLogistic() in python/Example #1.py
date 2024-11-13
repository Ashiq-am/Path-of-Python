# Import sympy and LogLogistic
from sympy.stats import LogLogistic, density
from sympy import Symbol, pprint

z = Symbol("z")
alpha = Symbol("alpha", positive = True)
beta = Symbol("beta", positive = True)

# Using sympy.stats.LogLogistic() method
X = LogLogistic("x", alpha, beta)
gfg = density(X)(z)

pprint(gfg)
