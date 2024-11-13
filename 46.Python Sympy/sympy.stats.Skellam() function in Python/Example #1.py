# import sympy, Skellam, density, Symbol
from sympy.stats import Skellam, density
from sympy import Symbol

mu1 = Symbol("mu1", positive = True)
mu2 = Symbol("mu2", positive = True)

# using sympy.stats.Skellam() method
X = Skellam("x", mu1, mu2)
skeDist = density(X)(z)

print(skeDist)
