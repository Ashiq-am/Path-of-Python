# import sympy, Multinomial, density, symbols
from sympy.stats.joint_rv_types import Multinomial
from sympy.stats import density
from sympy import symbols, pprint

x1, x2, x3 = symbols('x1, x2, x3', nonnegative = True, integer = True)
p1, p2, p3 = symbols('p1, p2, p3', positive = True)

# Using sympy.stats.Multinomial() method
M = Multinomial('M', 3, p1, p2, p3)
multiDist = density(M)(x1, x2, x3)

pprint(multiDist)
