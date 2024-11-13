# import totient() method from sympy
from sympy.ntheory.factor_ import totient

n = 24

# Use totient() method
totient_n = totient(n)

print("phi({}) = {} ".format(n, totient_n))  # 1 5 7 11 13 17 19 23
