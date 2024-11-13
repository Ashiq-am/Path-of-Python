# Import sympy and Moyal
from sympy.stats import Moyal, density, cdf
from sympy import Symbol, pprint

z = Symbol("z")
mu = Symbol("mu", positive = True)
sigma = Symbol("sigma", positive = True)

# Using sympy.stats.Moyal() method
X = Moyal("x", mu, sigma)
Z = density(X)(z)
gfg = simplify(cdf(X)(z))

print(gfg)
