# import sympy
from sympy import *

n = 6
k = 3
print("Value of n = {} and k = {}".format(n, k))

# Use sympy.fibonacci() method
nth_fibonacci_poly = fibonacci(n, k)

print("The nth fibonacci polynomial value : {}".format(nth_fibonacci_poly))
