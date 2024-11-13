# import reduced_totient() method from sympy
from sympy.ntheory import reduced_totient

n = 30

# Use reduced_totient() method
reduced_totient_n = reduced_totient(n)

print("lambda({}) = {} ".format(n, reduced_totient_n))
