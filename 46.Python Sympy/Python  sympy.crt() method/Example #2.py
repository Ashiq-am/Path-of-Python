# import crt() method from sympy
from sympy.ntheory.modular import crt

m = [99, 97, 95]
v = [49, 76, 65]

# Use crt() method
crt_m_v = crt(m, v)

print("Result of the Chinese Remainder Theorem = {} ".format(crt_m_v[0]))
