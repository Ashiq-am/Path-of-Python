# Import sympy and PowerFunction
from sympy.stats import PowerFunction, density, variance
from sympy import Symbol, pprint

z = Symbol("z")
alpha = 2
a = 0
b = 1

# Using sympy.stats.PowerFunction() method
X = PowerFunction("x", alpha, a, b)
gfg = density(X)(z)

pprint(variance(gfg))
