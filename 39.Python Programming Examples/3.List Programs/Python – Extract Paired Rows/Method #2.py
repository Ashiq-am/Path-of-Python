# Python3 code to demonstrate working of
# Extract Paired Rows
# Using filter() + lambda + count() + all()

# initializing list
test_list = [[10, 2, 3, 2, 3], [5, 5, 4, 7, 7, 4],
			[1, 2], [1, 1, 2, 2]]

# printing original list
print("The original list is : " + str(test_list))

# count() checks for frequency to be mod 2
# filter() and lambda used to perform filtering
res = list(filter(lambda row: all(
row.count(ele) % 2 == 0 for ele in row), test_list))

# printing result
print("Extracted rows : " + str(res))
