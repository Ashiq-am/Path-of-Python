# Python3 code to demonstrate working of
# K Dice Combinations
# Using list comprehension + product()
from itertools import product

# initializing K
K = 3

# using list comprehension to formulate elements
temp = [list(range(1, 7)) for _ in range(K)]

# using product() to get Combinations
res = list(product(*temp))

# printing result
print("The constructed dice Combinations : " + str(res))
