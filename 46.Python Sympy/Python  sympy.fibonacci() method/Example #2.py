# import sympy
from sympy import *

n = 5
k = symbols('x')
print("Value of n = {} and k = {}".format(n, k))

# Use sympy.fibonacci() method
nth_fibonacci_poly = fibonacci(n, k)

print("The nth fibonacci polynomial : {}".format(nth_fibonacci_poly))
