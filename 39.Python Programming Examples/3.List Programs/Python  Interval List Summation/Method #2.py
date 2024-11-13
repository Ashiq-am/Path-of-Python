# Python3 code to demonstrate
# Interval List Summation
# using itertools.compress() + itertools.cycle() + sum()
from itertools import compress, cycle

# initializing lists
test_list = list(range(50))

# printing original list
print("The original list is : " + str(test_list))

# interval elements
N = 5

# interval difference
K = 15

# using itertools.compress() + itertools.cycle() + sum()
# Interval List Summation
func = cycle([True] * N + [False] * (K - N))
res = sum(list(compress(test_list, func)))

# printing result
print("The modified range sum list : " + str(res))
