# Python3 code to demonstrate
# grouping like elements as list
# using itertools.groupby()
import itertools

# initializing list
test_list = [1, 3, 4, 2, 1, 3, 4, 2, 3, 4, 1]

# printing original list
print("The original list : " + str(test_list))

# using itertools.groupby()
# grouping like elements as list
res = [list(i) for j, i in itertools.groupby(sorted(test_list))]

# print result
print("The elements after grouping are : " + str(res))
