# Python3 code to demonstrate
# Case Insensitive Strings Grouping
# using sorted() + groupby()
from itertools import groupby

# initializing list
test_list = ['man', 'a', 'gEek', 'for', 'GEEK', 'FoR']

# printing original list
print("The original list : " + str(test_list))

# using sorted() + groupby()
# Case Insensitive Strings Grouping
util_func = lambda x: str.lower(x)
temp = sorted(test_list, key = util_func)
res = [list(ele) for i, ele in groupby(temp, util_func)]

# print result
print("The list after Categorization : " + str(res))
