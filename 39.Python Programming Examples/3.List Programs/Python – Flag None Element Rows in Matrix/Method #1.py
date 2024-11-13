# Python3 code to demonstrate working of
# Flag None Element Rows in Matrix
# Using list comprehension

# initializing list
test_list = [[2, 4, None, 3], [3, 4, 1, None], [2, 4, 7, 4], [2, 8]]

# printing original list
print("The original list is : " + str(test_list))

# in operator to check None value
# True if any None is found
res = [True if None in sub else False for sub in test_list]

# printing result
print("None Flagged List : " + str(res))
