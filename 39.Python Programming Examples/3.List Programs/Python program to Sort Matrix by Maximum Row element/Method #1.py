# Python3 code to demonstrate working of
# Sort Matrix by Maximum Row element
# Using sort() + max()

def max_sort(row):
	return max(row)

# initializing list
test_list = [[5, 7, 8], [9, 10, 3],
			[10, 18, 3], [0, 3, 5]]

# printing original list
print("The original list is : " + str(test_list))

# sort() for sorting, max to get maximum values
test_list.sort(key = max_sort, reverse = True)

# printing result
print("The maximum sorted Matrix : " + str(test_list))
