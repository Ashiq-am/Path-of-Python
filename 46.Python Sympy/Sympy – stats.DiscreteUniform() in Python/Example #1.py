# Import sympy and DiscreteUniform
from sympy.stats import DiscreteUniform, density
from sympy import symbols

# Using stats.DiscreteUniform() method
X = DiscreteUniform('X', symbols('g f g'))
gfg = density(X).dict

print(gfg)
