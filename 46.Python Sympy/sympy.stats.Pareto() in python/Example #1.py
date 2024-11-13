# Import sympy and Pareto
from sympy.stats import Pareto, density
from sympy import Symbol, pprint

z = Symbol("z")
xm = Symbol("xm", positive = True)
alpha = Symbol("alpha", positive = True)

# Using sympy.stats.Pareto() method
X = Pareto("x", xm, alpha)
gfg = density(X)(z)

pprint(gfg)
