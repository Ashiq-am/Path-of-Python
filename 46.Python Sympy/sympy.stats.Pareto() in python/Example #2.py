# Import sympy and Pareto
from sympy.stats import Pareto, density
from sympy import Symbol, pprint

z = 2.1
xm = 1
alpha = 2.4

# Using sympy.stats.Pareto() method
X = Pareto("x", xm, alpha)
gfg = density(X)(z)

pprint(gfg)
