# Python3 code to demonstrate working of
# Concatenate Rear elements in Tuple List
# Using map() + itemgetter() + join()
from operator import itemgetter

# initializing list
test_list = [(1, 2, "Gfg"), (4, "is"), ("Best", )]

# printing original list
print("The original list is : " + str(test_list))

# "-1" is used for access
# map() to get all elements
res = " ".join(list(map(itemgetter(-1), test_list)))

# printing result
print("The Concatenated result : " + str(res))
