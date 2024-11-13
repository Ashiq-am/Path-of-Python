# Python Program to explain math.prod() method

# Importing math module
import math

# If the given input iterable
# is empty, then this method
# returns the start value

# list
arr = []

# Calculate the product of
# of all elements present
# in the given list
product = math.prod(arr)
print(product)


# Tuple
tup = ()

# Calculate the product of
# of all elements present
# in the given tuple
product = math.prod(tup, start = 5)
print(product)
