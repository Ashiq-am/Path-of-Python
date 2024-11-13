# Python3 code to demonstrate
# Rear character String categorization
# using sorted() + groupby()
from itertools import groupby

# initializing list
test_list = ['an', 'apple', 'geek', 'for', 'greek', 'free']

# printing original list
print("The original list : " + str(test_list))

# using sorted() + groupby()
# Rear character String categorization
util_func = lambda x: x[len(x) - 1]
temp = sorted(test_list, key = util_func)
res = [list(ele) for i, ele in groupby(temp, util_func)]

# print result
print("The list after Categorization : " + str(res))
