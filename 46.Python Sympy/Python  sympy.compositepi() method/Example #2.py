# import compositepi() method from sympy
from sympy import compositepi

n = 100

# Use compositepi() method
count_composites = compositepi(n)

print("The number of composites numbers less than or equal to {} is {}".format(n, count_composites))
