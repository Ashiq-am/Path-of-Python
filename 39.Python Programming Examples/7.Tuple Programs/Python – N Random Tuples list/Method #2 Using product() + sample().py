# Python3 code to demonstrate working of
# N Random Tuples list
# Using product() + sample()
import random
import itertools

# initializing N
N = 5

# initializing Tuple element range
R = 10

# N Random Tuples list
# Using product() + sample()
res = random.sample(list(itertools.product(range(R + 1), repeat = 2)), N)

# printing result
print("The N random tuples : " + str(res))
