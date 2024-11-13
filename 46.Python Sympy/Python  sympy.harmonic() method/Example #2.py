# import sympy
from sympy import *

n = 5
m = 2
print("Value of n = {} and m = {}".format(n, m))

# Use sympy.harmonic() method
nth_harmonic_poly = harmonic(n, m)

print("The nth harmonic number of order m : {}".format(nth_harmonic_poly))
