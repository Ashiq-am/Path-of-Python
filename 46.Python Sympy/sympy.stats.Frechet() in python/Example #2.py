# Import sympy and Frechet
from sympy.stats import Frechet, density
from sympy import Symbol

a = 3
s = 1
m = -2
z = Symbol("z")

# Using sympy.stats.Frechet() method
X = Frechet("x", a, s, m)
gfg = density(X)(z)

print(gfg)
