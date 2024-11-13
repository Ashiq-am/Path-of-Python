# Import sympy and Wald
from sympy.stats import Wald, density
from sympy import Symbol, pprint

z = 0.86
mean = 6
lamda = 2.35

# Using sympy.stats.Wald() method
X = Wald("x", mean, lamda)
gfg = density(X)(z)

pprint(gfg)
