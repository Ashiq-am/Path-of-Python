# import udivisor_sigma() method from sympy
from sympy.ntheory.factor_ import udivisor_sigma

n = 12

# Use udivisor_sigma() method
udivisor_sigma_n = udivisor_sigma(n)

print("udivisor_sigma({}) = {} ".format(n, udivisor_sigma_n))
# 1 ^ 1 + 3 ^ 1 + 4 ^ 1 + 12 ^ 1 = 20
