# Import sympy and Zeta
from sympy.stats import Zeta, density, E, variance
from sympy import Symbol

s = 3
z = Symbol("z")

# Using sympy.stats.Zeta() method
X = Zeta("x", s)
gfg = density(X)(z)

print(gfg)
