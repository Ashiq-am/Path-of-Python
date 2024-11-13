# Import sympy and Yule-Simon
from sympy.stats import YuleSimon, density, E, variance
from sympy import Symbol, simplify

rho = 5
z = Symbol("z")

# Using sympy.stats.YuleSimon() method
X = YuleSimon("X", rho)
gfg = density(X)(z)

print(gfg)
