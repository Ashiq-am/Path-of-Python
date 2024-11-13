# Import sympy and Yule-Simon
from sympy.stats import YuleSimon, density, E, variance
from sympy import Symbol, simplify

rho = 5

# Using sympy.stats.YuleSimon() method
X = YuleSimon("X", rho)
gfg = density(X)(0.5)

print(gfg)
