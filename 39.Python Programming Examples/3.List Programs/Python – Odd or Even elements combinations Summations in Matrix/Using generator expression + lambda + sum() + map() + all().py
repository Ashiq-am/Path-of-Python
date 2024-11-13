# Python3 code to demonstrate working of
# Odd or Even elements combinations Summations in Matrix
# Using generator expression + lambda + sum() + map() + all()
from itertools import product

# initializing list
test_list = [[1, 5, 6], [7, 2, 4], [8, 9, 3]]

# printing original list
print("The original list is : " + str(test_list))

# Odd or Even elements combinations Summations in Matrix
# Using generator expression + lambda + sum() + map() + all()
temp1 = product(*test_list)
temp2 = (sub for sub in temp1 if all(ele % 2 == 0 for ele in sub)
		or all(ele % 2 == 1 for ele in sub))
res = {sum(map(lambda idx : idx, ele)) : ele for ele in temp2}

# printing result
print("The all possible sums are : " + str(res))
