# Import sympy and Rayleigh
from sympy.stats import Rayleigh, density
from sympy import Symbol, pprint

z = Symbol("z")
sigma = Symbol("sigma", positive = True)

# Using sympy.stats.Rayleigh() method
X = Rayleigh("x", sigma)
gfg = density(X)(z)

print(gfg)
