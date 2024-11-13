# Import sympy and Rayleigh
from sympy.stats import Rayleigh, density
from sympy import Symbol, pprint

z = 0.35
sigma = 2

# Using sympy.stats.Rayleigh() method
X = Rayleigh("x", sigma)
gfg = density(X)(z)

print(gfg)
