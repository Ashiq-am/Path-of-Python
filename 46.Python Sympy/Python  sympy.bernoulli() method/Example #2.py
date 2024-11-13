# import sympy
from sympy import *


n = 5
k = symbols('x')
print("Value of n = {} and k = {}".format(n, k))

# Use sympy.bernoulli() method
nth_bernoulli_poly = bernoulli(n, k)

print("The nth bernoulli polynomial : {}".format(nth_bernoulli_poly))
