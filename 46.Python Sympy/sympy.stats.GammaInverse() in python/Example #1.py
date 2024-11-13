# Import sympy and GammaInverse
from sympy.stats import GammaInverse, density
from sympy import Symbol

a = Symbol("a", integer = True, positive = True)
b = Symbol("b", integer = True, positive = True)
z = Symbol("z")

# Using sympy.stats.GammaInverse() method
X = GammaInverse("x", a, b)
gfg = density(X)(z)

print(gfg)
