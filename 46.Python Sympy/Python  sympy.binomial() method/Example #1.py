# import sympy
from sympy import *

N = 4
K = 2
print("N = {}, K = {}".format(N, K))

# Use sympy.binomial() method
comb = binomial(N, K)

print("N choose K : {}".format(comb))
