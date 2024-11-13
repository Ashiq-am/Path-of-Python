# import udivisor_sigma() method from sympy
from sympy.ntheory.factor_ import udivisor_sigma

n = 18
k = 2

# Use udivisor_sigma() method
udivisor_sigma_n = udivisor_sigma(n, k)

print("udivisor_sigma({}) = {} ".format(n, udivisor_sigma_n))
