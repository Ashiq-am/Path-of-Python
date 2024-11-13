# Python3 code to demonstrate
# Get last N elements from list
# using islice() + reversed()
from itertools import islice

# initializing list
test_list = [4, 5, 2, 6, 7, 8, 10]

# printing original list
print("The original list : " + str(test_list))

# initializing N
N = 5

# using islice() + reversed()
# Get last N elements from list
res = list(islice(reversed(test_list), 0, N))
res.reverse()

# print result
print("The last N elements of list are : " + str(res))
