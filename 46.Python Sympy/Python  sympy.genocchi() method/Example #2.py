# import sympy
from sympy import *

n = 10
print("Value of n = {}".format(n))

# Use sympy.genocchi() method
n_genocchi = [genocchi(x) for x in range(1, 11)]

print("N genocchi number are : {}".format(n_genocchi))
