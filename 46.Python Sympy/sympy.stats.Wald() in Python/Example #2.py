# Import sympy and Wald
from sympy.stats import Wald, density
from sympy import Symbol, pprint

z = Symbol("z")
mean = Symbol("mean", positive = True)
lamda = Symbol("lamda", positive = True)

# Using sympy.stats.Wald() method
X = Wald("x", mean, lamda)
gfg = density(X)(z)

pprint(gfg)
