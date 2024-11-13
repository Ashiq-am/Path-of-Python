# import sympy
from sympy import *

n = 6
k = 3
print("Value of n = {} and k = {}".format(n, k))

# Use sympy.tribonacci() method
nth_tribonacci_poly = tribonacci(n, k)

print("The nth tribonacci polynomial value : {}".format(nth_tribonacci_poly))
