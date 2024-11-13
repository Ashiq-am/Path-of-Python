# Python3 code to demonstrate working of
# Missing elements difference from Matrix and List
# Using sum() + from_iterable()
from itertools import chain

# initializing list
test_list = [[2, 4, 1], [8, 1, 2], [9, 1, 10], [4, 3, 2]]

# printing original list
print("The original list is : " + str(test_list))

# initializing target list
tar_list = [2, 3, 10, 7, 5, 4]

# flattening Matrix
flat_mat = list(chain.from_iterable(test_list))

# getting sum of list elements not in Matrix
list_sum = sum([ele for ele in tar_list if ele not in flat_mat])

# getting sum of Matrix elements not in list
mat_sum = sum([ele for ele in flat_mat if ele not in tar_list])

# computing difference
res = abs(mat_sum - list_sum)

# printing result
print("The computed count : " + str(res))
