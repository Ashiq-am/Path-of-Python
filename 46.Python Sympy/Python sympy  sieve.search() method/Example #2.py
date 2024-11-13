# import sympy
from sympy import sieve

# Use sieve.search() method
i, j = sieve.search(25)

print("The bounding prime indices of the number 23 : {}, {}".format(i, j))
