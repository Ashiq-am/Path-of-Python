# Python3 code to demonstrate
# Initial Character Case Categorization
# using sorted() + groupby()
from itertools import groupby

# initializing list
test_list = ['an', 'a', 'geek', 'for', 'g', 'free']

# printing original list
print("The original list : " + str(test_list))

# using sorted() + groupby()
# Initial Character Case Categorization
util_func = lambda x: x[0]
temp = sorted(test_list, key = util_func)
res = [list(ele) for i, ele in groupby(temp, util_func)]

# print result
print("The list after Categorization : " + str(res))
