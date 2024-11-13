# Import sympy and Arcsin
from sympy.stats import Arcsin, density
from sympy import Symbol, simplify

a = Symbol("a", real = True)
b = Symbol("b", real = True)
z = Symbol("z")

# Using sympy.stats.Arcsin() method
X = Arcsin("x", a, b)
gfg = density(X)(z)

print(gfg)
