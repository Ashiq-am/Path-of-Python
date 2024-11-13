# Python3 code to demonstrate
# Inverse K slice Sum
# using islice() + reversed() + sum()
from itertools import islice

# initializing list
test_list = [4, 5, 2, 6, 7, 8, 10]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 5

# using islice() + reversed() + sum()
# Inverse K slice Sum
res = list(islice(reversed(test_list), 0, K))
res.reverse()
res = sum(res)

# print result
print("The last K elements sum of list are : " + str(res))
