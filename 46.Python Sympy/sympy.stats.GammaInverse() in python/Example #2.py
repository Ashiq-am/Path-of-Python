# Import sympy and GammaInverse
from sympy.stats import GammaInverse, density
from sympy import Symbol

a = 4
b = 3
z = 2

# Using sympy.stats.GammaInverse() method
X = GammaInverse("x", a, b)
gfg = density(X)(z)

print(gfg)
