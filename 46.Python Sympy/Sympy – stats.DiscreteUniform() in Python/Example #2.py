# Import sympy and DiscreteUniform
from sympy.stats import DiscreteUniform, density
from sympy import symbols

# Using stats.DiscreteUniform() method
Y = DiscreteUniform('Y', list(range(5)))
gfg = density(Y).dict

print(gfg)
