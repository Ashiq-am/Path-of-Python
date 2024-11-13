# import sympy, NegativeMultinomia, density, symbols
from sympy.stats import density
from sympy.stats.joint_rv_types import NegativeMultinomial
from sympy import symbols, pprint

p1, p2, p3 = symbols('p1, p2, p3', positive = True)
x1, x2, x3 = symbols('x1, x2, x3', nonnegative = True, integer = True)

# using sympy.stats.NegativeMultinomial() method
N = NegativeMultinomial('N', 3, p1, p2, p3)
negMulti = density(N)(x1, x2, x3)

pprint(negMulti)
