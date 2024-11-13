# Python3 code to demonstrate
# Series K divisible elements
# using groupby() + any()
from itertools import groupby

# initializing list
test_list = [1, 5, 6, 4, 8, 12]

# printing original list
print("The original list : " + str(test_list))

# initializing N
N = 3

# initializing K
K = 4

# using groupby() + any()
# Series K divisible elements
res = any(len(list(sub)) == N for idx, sub in groupby([sub % K for sub in test_list]))

# print result
print("Does list contain the desired consecution : " + str(res))
