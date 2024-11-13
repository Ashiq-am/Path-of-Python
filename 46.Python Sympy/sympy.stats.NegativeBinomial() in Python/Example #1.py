# Import sympy and Negativebinomial
from sympy.stats import NegativeBinomial, density, E, variance
from sympy import Symbol, S

r = 5
p = S.One / 5

# Using sympy.stats.NegativeBinomial() method
X = NegativeBinomial("x", r, p)
gfg = density(X)(0.5)

print(gfg)
