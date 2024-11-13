# Import sympy and Uniform
from sympy.stats import Uniform, density
from sympy import Symbol, pprint

z = Symbol("z")
a = Symbol("a", positive = True)
b = Symbol("b", positive = True)

# Using sympy.stats.Uniform() method
X = Uniform("x", a, b)
gfg = density(X)(z)

pprint(gfg)
