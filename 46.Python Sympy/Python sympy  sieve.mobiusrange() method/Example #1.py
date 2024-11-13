# import sympy
from sympy import sieve

# Use sieve.mobiusrange() method
mobius_gen = sieve.mobiusrange(1, 10)
mobius_list = list(mobius_gen)

print("Mobius numbers for the range of numbers [1, 10) : {}".format(mobius_list))
