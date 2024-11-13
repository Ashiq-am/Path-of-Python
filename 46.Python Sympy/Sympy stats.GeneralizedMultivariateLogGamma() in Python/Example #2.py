# Import sympy and GeneralizedMultivariateLogGamma
from sympy.stats import density
from sympy.stats.joint_rv_types import GeneralizedMultivariateLogGamma
from sympy.stats.joint_rv import marginal_distribution
from sympy import symbols, S

v = 1
l, mu = [1, 2, 3], [2, 5, 1]
d = S.One
y = symbols('y_1:4', positive = True)

# Using sympy.stats.GeneralizedMultivariateLogGamma() method
Gd = GeneralizedMultivariateLogGamma('G', d, v, l, mu)
gfg = density(Gd)(y[0], y[1], y[2])

print(gfg)
