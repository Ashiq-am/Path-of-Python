# Import sympy and UniformSum
from sympy.stats import UniformSum, density
from sympy import Symbol, pprint

z = Symbol("z")
n = Symbol("n", positive = True)

# Using sympy.stats.UniformSum() method
X = UniformSum("x", n)
gfg = density(X)(z)

pprint(gfg)
