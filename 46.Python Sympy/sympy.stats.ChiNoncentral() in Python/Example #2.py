# Import sympy and ChiNoncentral
from sympy.stats import ChiNoncentral, density, E
from sympy import Symbol, simplify

k = 5
l = 6
z = 0.2

# Using sympy.stats.ChiNoncentral() method
X = ChiNoncentral("x", k, l)
gfg = density(X)(z)

print(gfg)
