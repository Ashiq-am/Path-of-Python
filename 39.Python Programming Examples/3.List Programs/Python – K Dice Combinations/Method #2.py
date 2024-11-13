# Python3 code to demonstrate working of
# K Dice Combinations
# Using repeat + product()
from itertools import product

# initializing K
K = 3

# using product() to get Combinations and repeat to get elements
res = list(product(range(1, 7), repeat = 3))

# printing result
print("The constructed dice Combinations : " + str(res))
