# Import sympy and Erlang
from sympy.stats import Erlang, density
from sympy import Symbol

k = 2
l = 3
z = 1

# Using sympy.stats.Erlang() method
X = Erlang("x", k, l)
gfg = density(X)(z)

print(gfg)
