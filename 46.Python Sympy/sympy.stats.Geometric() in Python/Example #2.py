# Import sympy and geometric
from sympy.abc import z
from sympy.stats import Geometric, density, E, variance
from sympy import Symbol, S

# Using sympy.stats.Geometric() method
X = Geometric("x", 0.4)
gfg = density(X)(z)

print(variance(X))
