# Import sympy and LogLogistic
from sympy.stats import LogLogistic, density
from sympy import Symbol, pprint

z = 1.2
alpha = 2
beta = 3

# Using sympy.stats.LogLogistic() method
X = LogLogistic("x", alpha, beta)
gfg = density(X)(z)

pprint(gfg)
