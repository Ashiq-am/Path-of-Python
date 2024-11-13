# import sympy
from sympy import *

n = 7
print("Value of n = {}".format(n))

# Use sympy.partition() method
nth_partition = partition(n)

print("Value of nth partition number : {}".format(nth_partition))
