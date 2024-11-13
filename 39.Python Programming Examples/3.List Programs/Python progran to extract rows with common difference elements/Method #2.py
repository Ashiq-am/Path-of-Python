# Python3 code to demonstrate working of
# all() + list comprehension
# Using list comprehension + all()

# initializing list
test_list = [[4, 7, 10],
			[8, 10, 12],
			[10, 11, 13],
			[6, 8, 10]]

# printing original list
print("The original list is : " + str(test_list))

# checking for all values to have common difference
res = [row for row in test_list
	if all(row[idx + 1] - row[idx] == row[1] - row[0]
			for idx in range(0, len(row) - 1))]

# printing result
print("Filtered Matrix : " + str(res))
