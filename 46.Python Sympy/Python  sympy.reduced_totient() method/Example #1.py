# import reduced_totient() method from sympy
from sympy.ntheory import reduced_totient

n = 8

# Use reduced_totient() method
reduced_totient_n = reduced_totient(n)

print("lambda({}) = {} ".format(n, reduced_totient_n))
# 1 ^ 2 = 1 (mod 8), 3 ^ 2 = 9 = 1 (mod 8),
# 5 ^ 2 = 25 = 1 (mod 8) and 7 ^ 2 = 49 = 1 (mod 8)
