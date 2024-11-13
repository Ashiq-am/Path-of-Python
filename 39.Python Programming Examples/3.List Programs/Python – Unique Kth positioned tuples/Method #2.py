# Python3 code to demonstrate working of
# Unique Kth index tuples
# Using next() + groupby() + lambda
from itertools import groupby

# initializing list
test_list = [(5, 6, 8), (4, 2, 7), (1, 2, 3), (9, 6, 5)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# Unique Kth index tuples
# Using next() + groupby() + lambda
temp = lambda ele : ele[K - 1]
res = [next(val) for _, val in groupby(sorted(test_list, key = temp), key = temp)]

# printing result
print("The extracted elements : " + str(res))
