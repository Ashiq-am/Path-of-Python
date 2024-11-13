# import sympy, NormalGamma, density, symbols
from sympy.stats import density, NormalGamma
from sympy import symbols, pprint

y, z = symbols('y z')

# using sympy.stats.NormalGamma() method
X = NormalGamma('X', 1 / 2, 3, 4, 6)
norGammaDist = density(X)(y, z)

pprint(norGammaDist)
