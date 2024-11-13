# Import sympy and GeneralizedMultivariateLogGammaOmega
from sympy.stats import density
from sympy.stats.joint_rv_types import GeneralizedMultivariateLogGammaOmega
from sympy.stats.joint_rv import marginal_distribution
from sympy import symbols, S, Matrix

v = 1
l, mu = [1, 2], [2, 1]
d = S.One
y = symbols('y_1:3', positive = True)
omega = Matrix([[1, S.Half], [S.Half, 1]])

# Using sympy.stats.GeneralizedMultivariateLogGammaOmega() method
Gd = GeneralizedMultivariateLogGammaOmega('G', omega, v, l, mu)
gfg = density(Gd)(y[0], y[1])

pprint(gfg)
