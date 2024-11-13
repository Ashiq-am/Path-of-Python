# Import sympy and Logistic
from sympy.stats import Logistic, density
from sympy import Symbol, pprint

z = 0.3
mu = 5
s = 1.3

# Using sympy.stats.Logistic() method
X = Logistic("x", mu, s)
gfg = density(X)(z)

pprint(gfg)
