# import sympy
from sympy import *

X = symbols('x')
print("X = {}".format(X))

# Use sympy.gamma() method
gamma_X = gamma(X)

print("gamma(X) : {}".format(gamma_X))
