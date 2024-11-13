# Python3 code to demonstrate working of
# All Possible unique K size combinations till N
# Using product() + setdefault() + loop
from itertools import product

# initializing N
N = 4

# Initialize K
K = 3

# All Possible unique K size combinations till N
# Using product() + setdefault() + loop
temp = list(product(range(N), repeat = K))
res = {}
for tup in temp:
	key = tuple(sorted(tup))
	res.setdefault(key, []).append(tup)
res = list(res.keys())

# printing result
print("The unique combinations : " + str(res))
