# Python Program to explain math.prod() method

# Importing math module
import math


# By default start value is 1
# but can be explicitly provided
# as a named (keyword-only) parameter

# list
arr = [1, 2, 3, 4, 5]

# Calculate the product of
# of all elements present
# in the given list
product = math.prod(arr, start = 2)
print(product)
