# Import sympy and Negativebinomial
from sympy.stats import NegativeBinomial, density, E, variance
from sympy import Symbol, S

r = 4
p = 0.6
z = Symbol("z")

# Using sympy.stats.NegativeBinomial() method
X = NegativeBinomial("x", r, p)
gfg = density(X)(z)

print(gfg)
