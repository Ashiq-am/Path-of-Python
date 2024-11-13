# Python3 code to demonstrate
# Grouping Anagrams
# using list comprehension + sorted() + lambda + groupby()
from itertools import groupby

# initializing list
test_list = ['lump', 'eat', 'me', 'tea', 'em', 'plum']

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + sorted() + lambda + groupby()
# Grouping Anagrams
temp = lambda test_list: sorted(test_list)
res = [list(val) for key, val in groupby(sorted(test_list, key = temp), temp)]

# print result
print("The grouped Anagrams : " + str(res))
