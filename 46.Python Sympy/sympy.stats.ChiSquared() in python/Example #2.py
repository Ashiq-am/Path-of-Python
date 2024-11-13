# Import sympy and chisquared
from sympy.stats import ChiSquared, density
from sympy import Symbol

k = 3
z = 2

# Using sympy.stats.ChiSquared() method
X = ChiSquared("x", k)
gfg = density(X)(z)

print(gfg)
