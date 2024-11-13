# import sympy
from sympy import sieve

# Use sieve.primerange() method
prime_gen = sieve.primerange(1, 10)
prime_list = list(prime_gen)

print("Prime numbers for the range of numbers [1, 10) : {}".format(prime_list))
