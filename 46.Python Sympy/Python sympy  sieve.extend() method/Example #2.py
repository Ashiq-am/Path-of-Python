# import sympy
from sympy import sieve

# Use sieve.extend() method
sieve.extend(100)
prime_list = sieve._list

print("Prime Numbers up to 100 : {}".format(prime_list))
