# Python3 code to demonstrate working of
# K length groups with given summation
# Using sum + product()
from itertools import product

# initializing list
test_list = [6, 3, 12, 7, 4, 11]

# printing original list
print("The original list is : " + str(test_list))

# initializing Summation
N = 21

# initializing size
K = 4

# Looping for each product and comparing with required summation
res = []
for sub in product(test_list, repeat=K):
    if sum(sub) == N:
        res.append(sub)

# printing result
print("The sublists with of given size and sum : " + str(res))
