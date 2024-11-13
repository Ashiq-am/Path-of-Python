# import sympy
from sympy import *

n = 5
k = symbols('x')
print("Value of n = {} and k = {}".format(n, k))

# Use sympy.tribonacci() method
nth_tribonacci_poly = tribonacci(n, k)

print("The nth tribonacci polynomial : {}".format(nth_tribonacci_poly))
