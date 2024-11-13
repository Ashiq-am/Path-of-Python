# Python3 code to demonstrate working of
# Extract String elements from Mixed Matrix
# Using chain.from_iterables + list comprehension + isinstance()
from itertools import chain

# initializing lists
test_list = [[5, 6, 3], ["Gfg", 3, "is"], [9, "best", 4]]

# printing original list
print("The original list : " + str(test_list))

# strings are extracted using isinstance()
# using chain.from_iterables()
res = [ele for ele in chain.from_iterable(test_list) if isinstance(ele, str)]

# printing result
print("The String instances : " + str(res))
