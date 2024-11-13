# import sympy
from sympy import sieve

# Use sieve.extend() method
sieve.extend(50)
prime_list = sieve._list

print("Prime Numbers up to 50 : {}".format(prime_list))
