# import primefactors() method from sympy
from sympy import primefactors

n = -210

# Use primefactors() method
primefactors_n = primefactors(n)

print("The prime factors of {} : {}".format(n, primefactors_n))
