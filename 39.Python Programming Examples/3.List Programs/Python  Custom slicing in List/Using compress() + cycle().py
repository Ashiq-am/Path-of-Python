# Python3 code to demonstrate working of
# Custom slicing in List
# using compress() + cycle()
from itertools import cycle, compress

# initialize lists
test_list = [1, 2, 4, 7, 3, 8, 6, 2, 10, 11, 17, 34, 23, 21]

# printing original list
print("The original list is : " + str(test_list))

# initialize interval
interval = 5

# initialize element number
ele_num = 4

# Custom slicing in List
# using compress() + cycle()
temp = cycle([True] * ele_num + [False] * interval)
res = list(compress(test_list, temp))

# printing result
print("Custom sliced list is : " + str(res))
