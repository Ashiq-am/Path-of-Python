# Python3 code to demonstrate
# Sorting list of lists with similar list elements
# using map() + sorted()

# initializing list
test_list = [[[4, 4], [1, 1]], [[3, 3], [2, 2], [5, 5]]]

# printing original list
print("The original list : " + str(test_list))

# using map() + sorted()
# Sorting list of lists with similar list elements
res = list(map(sorted, test_list))

# print result
print("The list after performing sort operation : " + str(res))
