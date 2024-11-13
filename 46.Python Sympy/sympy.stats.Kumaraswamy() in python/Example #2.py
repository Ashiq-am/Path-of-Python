# Import sympy and Kumaraswamy
from sympy.stats import Kumaraswamy, density
from sympy import Symbol, pprint

z = 0.3
a = 2
b = 6

# Using sympy.stats.Kumaraswamy() method
X = Kumaraswamy("x", a, b)
gfg = density(X)(z)

pprint(gfg)
