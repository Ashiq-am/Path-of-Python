# Python3 code to demonstrate working of
# Flag None Element Rows in Matrix
# Using all() + list comprehension

# initializing list
test_list = [[2, 4, None, 3], [3, 4, 1, None], [2, 4, 7, 4], [2, 8]]

# printing original list
print("The original list is : " + str(test_list))

# all() checks for all non none values
res = [False if all(sub) else True for sub in test_list]

# printing result
print("None Flagged List : " + str(res))
