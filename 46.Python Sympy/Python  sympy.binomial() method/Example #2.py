# import sympy
from sympy import *

N, K = symbols('A B')

print("N = {}, K = {}".format(N, K))

# Use sympy.binomial() method
comb = binomial(N, K)

print("N choose K : {}".format(comb))
