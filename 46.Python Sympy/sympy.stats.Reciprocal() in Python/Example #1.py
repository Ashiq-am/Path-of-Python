# Import sympy and Reciprocal
from sympy.stats import Reciprocal, density
from sympy import Symbol, pprint

z = Symbol("z")
a = Symbol("a", positive = True)
b = Symbol("b", positive = True)

# Using sympy.stats.Reciprocal() method
X = Reciprocal("x", a, b)
gfg = density(X)(z)

print(gfg)
