# Python3 code to demonstrate working of
# K length Concatenate Single Valued Tuple
# Using zip_longest() + chain.from_iterables()
from itertools import chain, zip_longest

# initializing lists
test_list = [(3, ), (6, ), (8, ), (2, ), (9, ), (4, )]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

# K length Concatenate Single Valued Tuple
# Using zip() + list comprehension
temp = [iter(chain.from_iterable(test_list))] * K
res = list(zip_longest(*temp))

# printing result
print("Concatenated tuples : " + str(res))
