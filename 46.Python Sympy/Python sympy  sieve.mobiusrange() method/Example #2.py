# import sympy
from sympy import sieve

# Use sieve.mobiusrange() method
mobius_gen = sieve.mobiusrange(8, 20)
mobius_list = list(mobius_gen)

print("Mobius numbers for the range of numbers [8, 20) : {}".format(mobius_list))
