# import primepi() method from sympy
from sympy import primepi

n = 10

# Use primepi() method
count_primes = primepi(n)

print("The number of prime numbers less than or equal to {} is {}".format(n, count_primes))
