# Python3 code to demonstrate
# list frequency of elements
# using Counter() + set() + list comprehension
from collections import Counter

# initializing list
test_list = [[3, 5, 4],
			[6, 2, 4],
			[1, 3, 6]]

# printing original list
print("The original list : " + str(test_list))

# using Counter() + set() + list comprehension
# list frequency of elements
res = dict(Counter(i for sub in test_list for i in set(sub)))

# printing result
print("The list frequency of elements is : " + str(res))
