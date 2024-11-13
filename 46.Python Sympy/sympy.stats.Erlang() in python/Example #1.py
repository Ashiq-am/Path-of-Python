# Import sympy and Erlang
from sympy.stats import Erlang, density
from sympy import Symbol

k = Symbol("k", integer = True, positive = True)
l = Symbol("l", integer = True, positive = True)
z = Symbol("z")

# Using sympy.stats.Erlang() method
X = Erlang("x", k, l)
gfg = density(X)(z)

print(gfg)
