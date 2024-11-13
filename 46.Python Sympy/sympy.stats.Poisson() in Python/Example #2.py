# Import sympy and poisson
from sympy.stats import Poisson, density, E, variance
from sympy import Symbol, simplify

# Using sympy.stats.Poisson() method
rate = Symbol("lambda", positive = True)
X = Poisson("x", rate)
gfg = density(X)(6)

print(gfg)
