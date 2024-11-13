# import totient() method from sympy
from sympy.ntheory.factor_ import totient

n = 19

# Use totient() method
totient_n = totient(n)

print("phi({}) = {} ".format(n, totient_n))
