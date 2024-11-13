# Python3 code to demonstrate working of
# Consecutive remaining elements in list
# using range() + from_iterable() + groupby() + list comprehension
from itertools import chain, groupby

# initialize list
test_list = [4, 4, 5, 5, 5, 1, 1, 2, 4]

# printing original list
print("The original list is : " + str(test_list))

# Consecutive remaining elements in list
# using range() + from_iterable() + groupby() + list comprehension
temp = (range(len(list(j)), 0, -1) for i, j in groupby(test_list))
res = list(chain.from_iterable(temp))

# printing result
print("Consecutive remaining elements list : " + str(res))
