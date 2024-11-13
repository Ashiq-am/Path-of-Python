# Import sympy and Reciprocal
from sympy.stats import Reciprocal, density
from sympy import Symbol, pprint

z = 0.35
a = 1
b = 2

# Using sympy.stats.Reciprocal() method
X = Reciprocal("x", a, b)
gfg = density(X)(z)

print(gfg)
