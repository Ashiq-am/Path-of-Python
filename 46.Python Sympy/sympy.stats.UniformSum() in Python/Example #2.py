# Import sympy and UniformSum
from sympy.stats import UniformSum, density
from sympy import Symbol, pprint

z = 3
n = 5

# Using sympy.stats.UniformSum() method
X = UniformSum("x", n)
gfg = density(X)(z)

pprint(gfg)
