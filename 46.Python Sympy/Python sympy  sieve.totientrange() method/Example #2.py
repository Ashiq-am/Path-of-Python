# import sympy
from sympy import sieve

# Use sieve.totientrange() method
totient_gen = sieve.totientrange(8, 20)
totient_list = list(totient_gen)

print("Totient numbers for the range of numbers [8, 20) : {}".format(totient_list))
