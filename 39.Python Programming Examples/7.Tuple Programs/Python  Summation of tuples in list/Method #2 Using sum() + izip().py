# Python3 code to demonstrate working of
# Summation of tuples in list
# using sum() + izip()
from itertools import izip

# initialize list of tuple
test_list = [(1, ), (5, ), (2, )]

# printing original tuples list
print("The original list : " + str(test_list))

# Summation of tuples in list
# using sum() + map()
res = sum(*izip(*test_list))

# printing result
print("The summation of all tuple elements are : " + str(res))
