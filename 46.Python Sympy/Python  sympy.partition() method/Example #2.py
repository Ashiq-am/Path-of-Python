# import sympy
from sympy import *

n = 10
print("Value of n = {}".format(n))

# Use sympy.partition() method
n_partition = [partition(x) for x in range(1, 11)]

print("N partition number are : {}".format(n_partition))
