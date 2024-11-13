# Python3 code to demonstrate working of
# Test if greater than preceding element in Tuple List
# Using tee() + zip() + list comprehension
from itertools import tee


# helper function
def pair(test_list):
    # pairing elements in 2 sized tuple
    x, y = tee(test_list)
    next(y, None)
    return zip(x, y)


# initializing list
test_list = [(3, 5, 1), (7, 4, 9), (1, 3, 5)]

# printing original list
print("The original list : " + str(test_list))

# Test if greater than preceding element in Tuple List
# Using tee() + zip() + list comprehension
res = []
for sub in test_list:
    # appending result by checking with Dual Pairs
    res.append(tuple((False,)) + tuple([x < y for x, y in pair(sub)]))

# printing result
print("Filtered values : " + str(res))
