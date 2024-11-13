# import sympy, MultivariateBeta, density, Symbol
from sympy.stats.joint_rv_types import MultivariateBeta
from sympy.stats import density
from sympy import Symbol, pprint

a = Symbol('a', positive = True)
b = Symbol('b', positive = True)
x = Symbol('x')
y = Symbol('y')

# using sympy.stats.MultivariateBeta() method
M = MultivariateBeta('M', [a, b])
mvbDist = density(M)(x, y)

pprint(mvbDist)
