# Python3 code to demonstrate working of
# Tuple to Dictionary Summation conversion
# Using dictionary comprehension + sum() + groupby()
from itertools import groupby

# initializing list
test_list = [(7, 8), (5, 6), (7, 2), (6, 8), (5, 10)]

# printing original list
print("The original list is : " + str(test_list))

# Tuple to Dictionary Summation conversion
# Using dictionary comprehension + sum() + groupby()
fnc = lambda ele: ele[0]
res = {key: sum(sub[1] for sub in val) for key, val in groupby(
					sorted(test_list, key = fnc), key = fnc)}

# printing result
print("The summation tuple dictionary : " + str(res))
