# import sympy, MultivariateBeta, density, Symbol
from sympy.stats.joint_rv_types import MultivariateBeta
from sympy.stats import density
from sympy import Symbol, pprint

x = Symbol('x')
y = Symbol('y')

# using sympy.stats.MultivariateBeta() method
M = MultivariateBeta('M', [2, 1 / 2])
mvbDist = density(M)(x, y)

pprint(mvbDist)
