# Import sympy and Uniform
from sympy.stats import Uniform, density
from sympy import Symbol, pprint

z = 0.3
a = -3
b = 4

# Using sympy.stats.Uniform() method
X = Uniform("x", a, b)
gfg = density(X)(z)

pprint(gfg)
