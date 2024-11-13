# Python3 code to demonstrate working of
# N Random Tuples list
# Using list comprehension + sample()
import random

# initializing N
N = 5

# initializing Tuple element range
R = 10

# N Random Tuples list
# Using list comprehension + sample()
res = [divmod(ele, R + 1) for ele in random.sample(range((R + 1) * (R + 1)), N)]

# printing result
print("The N random tuples : " + str(res))
