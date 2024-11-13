# import primeomega() method from sympy
from sympy.ntheory.factor_ import primeomega

n = 120

# Use primeomega() method
primeomega_n = primeomega(n)

print(" Number of prime factors of {} = {} ".format(n, primeomega_n))
