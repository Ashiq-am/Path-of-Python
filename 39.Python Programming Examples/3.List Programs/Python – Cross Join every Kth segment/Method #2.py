# Python3 code to demonstrate working of
# Cross Join every Kth segment
# Using zip_longest() + list comprehension
from itertools import zip_longest, chain

# initializing lists
test_list1 = [4, 3, 8, 2, 6, 7]
test_list2 = [5, 6, 7, 4, 3, 1]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# initializing K
K = 2

# zip_longest to get segments
res = [y for idx in zip(zip_longest(*[iter(test_list1)] * K),
	zip_longest(*[iter(test_list2)] * K)) for y in chain.from_iterable(idx) if y]

# printing result
print("The cross joined list : " + str(res))
