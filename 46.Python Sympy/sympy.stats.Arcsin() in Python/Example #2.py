# Import sympy and Arcsin
from sympy.stats import Arcsin, density
from sympy import Symbol, simplify

a = -4
b = 8
z = Symbol("z")

# Using sympy.stats.Arcsin() method
X = Arcsin("x", a, b)
gfg = density(X)(z)

print(gfg)
