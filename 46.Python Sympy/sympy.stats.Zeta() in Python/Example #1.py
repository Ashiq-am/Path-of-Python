# Import sympy and Zeta
from sympy.stats import Zeta, density, E, variance
from sympy import Symbol

s = 7

# Using sympy.stats.Zeta() method
X = Zeta("x", s)
gfg = density(X)(0.33333)

print(gfg)
