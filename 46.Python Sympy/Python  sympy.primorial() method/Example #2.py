# import primorial() method from sympy
from sympy import primorial

n = 10

# Use primorial() method
primorial_n = primorial(n, nth=False)  # 2 * 3 * 5 * 7

print("The product of primes less than or equal to {} is {}".format(n, primorial_n))
