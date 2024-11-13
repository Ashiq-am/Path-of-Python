# Python3 code to demonstrate
# Prefix Sum Subarray till False value
# from_iterable() + accumulate() + groupby()
from itertools import groupby, accumulate, chain

# initializing list of lists
test_list = [1, 3, 4, 0, 4, 5, 0, 7, 8]

# printing original list
print ("The original list is : " + str(test_list))

# Prefix Sum Subarray till False value
# from_iterable() + accumulate() + groupby()
res = list(chain.from_iterable(accumulate(j)
			for i, j in groupby(test_list, bool)))

# printing result
print ("The computed modified new list : " + str(res))
