# Python3 code to demonstrate working of
# K sized N random elements
# Using product() + sample()
from random import sample
import itertools

# initializing list
test_list = [6, 9, 1, 8, 4, 7]

# initializing K, N
K, N = 3, 4

# printing original list
print("The original list is : " + str(test_list))

# get all permutations
temp = (idx for idx in itertools.product(test_list, repeat=K))

# get Random N from them
res = sample(list(temp), N)
res = list(map(list, res))

# printing result
print("K sized N random lists : " + str(res))
