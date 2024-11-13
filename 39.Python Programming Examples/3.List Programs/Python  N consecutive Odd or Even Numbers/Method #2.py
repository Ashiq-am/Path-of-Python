# Python3 code to demonstrate
# N consecutive Odd or Even Numbers
# using groupby() + any()
from itertools import groupby

# initializing list
test_list = [1, 5, 6, 4, 8]

# printing original list
print("The original list : " + str(test_list))

# initializing N
N = 3

# using groupby() + any()
# N consecutive Odd or Even Numbers
res = any(len(list(sub)) == N for idx, sub in
	groupby([sub % 2 for sub in test_list]))

# print result
print("Does list contain the desired consecution : " + str(res))
