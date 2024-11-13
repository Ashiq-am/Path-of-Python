# Python3 code to demonstrate working of
# Cross tuple summation grouping
# Using groupby() + sum() + zip() + list comprehension
from itertools import groupby

# initializing list
test_list = [(4, 5), (7, 5), (8, 6), (10, 6), (10, 4), (6, 7), (3, 7)]

# printing original list
print("The original list is : " + str(test_list))

# Concatenate Similar Key values
# Using groupby() + sum() + zip() + list comprehension
res = [(sum(next(zip(*ele))), key) for key, ele in groupby(
					test_list, key = lambda tup:tup[1])]

# printing result
print("The grouped records are : " + str(res))
