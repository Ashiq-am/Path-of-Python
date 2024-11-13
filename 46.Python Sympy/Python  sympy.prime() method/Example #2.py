# import sympy
from sympy import prime

n = 23

# Use prime() method
nth_prime = prime(n)

print("The {}rd prime is {}".format(n, nth_prime))
