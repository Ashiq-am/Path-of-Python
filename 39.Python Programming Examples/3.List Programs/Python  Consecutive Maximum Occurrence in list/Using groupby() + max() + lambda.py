# Python3 code to demonstrate working of
# Consecutive Maximum Occurrence in list
# using groupby() + max() + lambda
from itertools import groupby

# initializing list
test_list = [1, 1, 1, 2, 2, 4, 2, 2, 5, 5, 5, 5]

# printing original list
print("The original list is : " + str(test_list))

# Consecutive Maximum Occurrence in list
# using groupby() + max() + lambda
temp = groupby(test_list)
res = max(temp, key = lambda sub: len(list(sub[1])))

# printing result
print("Maximum Consecutive Occurring number is : " + str(res[0]))
