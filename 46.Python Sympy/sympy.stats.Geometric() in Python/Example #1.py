# Import sympy and geometric
from sympy.abc import z
from sympy.stats import Geometric, density, E, variance
from sympy import Symbol, S

p = S.One / 5

# Using sympy.stats.Geometric() method
X = Geometric("x", p)
gfg = density(X)(z)

print(variance(X))
