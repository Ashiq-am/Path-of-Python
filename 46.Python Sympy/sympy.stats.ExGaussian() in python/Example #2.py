# Import sympy and ExGaussian
from sympy.stats import ExGaussian, density
from sympy import Symbol

mean = 22
std = 21
rate = 7
z = 0.4

# Using sympy.stats.ExGaussian() method
X = ExGaussian("x", mean, std, rate)
gfg = density(X)(z)

print(gfg)
