# Python3 code to demonstrate
# Consecutive Custom Chunked elements Product
# using itertools.compress() + itertools.cycle() + loop
from itertools import compress, cycle


# getting Product
def prod(val):
    res = 1
    for ele in val:
        res *= ele
    return res


# initializing lists
test_list = list(range(1, 50))

# printing original list
print("The original list is : " + str(test_list))

# interval elements
N = 5

# interval difference
K = 15

# using itertools.compress() + itertools.cycle() + loop
# Consecutive Custom Chunked elements Product
func = cycle([True] * N + [False] * (K - N))
res = prod(list(compress(test_list, func)))

# printing result
print("The modified range product list : " + str(res))
