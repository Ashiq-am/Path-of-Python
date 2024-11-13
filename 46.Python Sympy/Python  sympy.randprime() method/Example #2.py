# import randprime() method from sympy
from sympy import randprime

a = 60
b = 100

# Use randprime() method
a_randprime_b = randprime(a, b)

print("A random prime between {} and {} is {}".format(a, b, a_randprime_b))
