# import sympy
from sympy import sieve

# Use sieve.primerange() method
prime_gen = sieve.primerange(8, 50)
prime_list = list(prime_gen)

print("Prime numbers for the range of numbers [8, 50) : {}".format(prime_list))
