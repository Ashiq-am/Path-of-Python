# import primorial() method from sympy
from sympy import primorial

n = 3

# Use primorial() method
primorial_n = primorial(n)  # 2 * 3 * 5

print("The product of first {} primes is {}".format(n, primorial_n))
