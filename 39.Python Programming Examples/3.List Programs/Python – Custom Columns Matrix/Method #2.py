# Python3 code to demonstrate working of
# Custom Columns Matrix
# Using itemgetter() + list comprehension
from operator import itemgetter

# initializing list
test_list = [[5, 4, 3, 4],
			[7, 6, 3, 2],
			[8, 3, 9, 10]]

# printing original list
print("The original list : " + str(test_list))

# initializing Columns list
col_list = [1, 3]

# Custom Columns Matrix
# Using itemgetter() + list comprehension
res = [list(itemgetter(*col_list)(ele)) for ele in test_list]

# printing result
print("Matrix after filtering : " + str(res))
