# Import sympy and FDistribution
from sympy.stats import FDistribution, density
from sympy import Symbol

d1 = 5
d2 = 6
z = 1

# Using sympy.stats.FDistribution() method
X = FDistribution("x", d1, d2)
gfg = density(X)(z)

print(gfg)
