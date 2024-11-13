# Import sympy and ChiNoncentral
from sympy.stats import ChiNoncentral, density, E
from sympy import Symbol, simplify

k = Symbol("k", integer = True)
l = Symbol("l", integer = True)
z = Symbol("z")

# Using sympy.stats.ChiNoncentral() method
X = ChiNoncentral("x", k, l)
gfg = density(X)(z)

print(gfg)
