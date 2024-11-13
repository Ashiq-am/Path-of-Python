# Import sympy and Frechet
from sympy.stats import Frechet, density
from sympy import Symbol

a = Symbol("a", integer = True, positive = True)
s = Symbol("s", integer = True, positive = True)
m = Symbol("m", integer = True, positive = True)
z = Symbol("z")

# Using sympy.stats.Frechet() method
X = Frechet("x", a, s, m)
gfg = density(X)(z)

print(gfg)
