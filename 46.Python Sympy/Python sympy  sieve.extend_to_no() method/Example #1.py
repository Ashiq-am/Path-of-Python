# import sympy
from sympy import sieve

# Use sieve.extend_to_no() method
sieve.extend_to_no(15)
prime_list = sieve._list

print("Prime Numbers up to 15th prime : {}".format(prime_list))
