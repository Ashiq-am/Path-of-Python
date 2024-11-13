# Python3 code to demonstrate
# interval initializing in list
# using itertools.compress() + itertools.cycle()
from itertools import compress, cycle

# initializing lists
test_list = list(range(50))

# printing original list
print("The original list is : " + str(test_list))

# interval elements
N = 5

# interval difference
K = 15

# using itertools.compress() + itertools.cycle()
# interval initializing in list
func = cycle([True] * N + [False] * (K - N))
res = list(compress(test_list, func))

# printing result
print("The modified initialized list : " + str(res))
