# import sympy, NegativeMultinomia, density, symbols
from sympy.stats import density
from sympy.stats.joint_rv_types import NegativeMultinomial
from sympy import symbols, pprint

x1, x2, x3 = symbols('x1, x2, x3', nonnegative = True, integer = True)

# using sympy.stats.NegativeMultinomial() method
N = NegativeMultinomial('N', 2, 1 / 3, 1 / 2)
negMulti = density(N)(x1, x2, x3)

pprint(negMulti)
