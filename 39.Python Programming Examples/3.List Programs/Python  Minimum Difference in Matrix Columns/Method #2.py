# Python3 code to demonstrate
# Minimum Difference in Matrix Columns
# using min() + map() + abs + zip()

# initializing list
test_list = [[3, 4, 5], [4, 6, 8], [1, 9, 2], [3, 7, 10]]

# printing original list
print("The original list : " + str(test_list))

# using min() + map() + abs + zip()
# Minimum absolute difference list of list
res = [min(map(abs, (i - j for i, j in zip(x, y)))) for x, y in zip(test_list, test_list[1:])]

# print result
print("The minimum difference sublist : " + str(res))
