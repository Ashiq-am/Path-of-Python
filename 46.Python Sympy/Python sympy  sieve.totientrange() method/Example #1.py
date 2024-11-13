# import sympy
from sympy import sieve

# Use sieve.totientrange() method
totient_gen = sieve.totientrange(1, 10)
totient_list = list(totient_gen)

print("Totient numbers for the range of numbers [1, 10) : {}".format(totient_list))
