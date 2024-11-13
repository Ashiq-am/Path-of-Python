# Python3 code to demonstrate working of
# Extract Paired Rows
# Using all() + list comprehension + count()

# initializing list
test_list = [[10, 2, 3, 2, 3], [5, 5, 4, 7, 7, 4],
			[1, 2], [1, 1, 2, 2]]

# printing original list
print("The original list is : " + str(test_list))

# count() checks for frequency to be mod 2
res = [row for row in test_list if all(
row.count(ele) % 2 == 0 for ele in row)]

# printing result
print("Extracted rows : " + str(res))
