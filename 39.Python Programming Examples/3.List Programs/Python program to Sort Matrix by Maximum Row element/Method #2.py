# Python3 code to demonstrate working of
# Sort Matrix by Maximum Row element
# Using sorted() + lambda + max()

# initializing list
test_list = [[5, 7, 8], [9, 10, 3],
			[10, 18, 3], [0, 3, 5]]

# printing original list
print("The original list is : " + str(test_list))

# sorted() for sorting, max to get maximum values
# reverse for reversed order
res = sorted(test_list, key = lambda row : max(row), reverse=True)

# printing result
print("The maximum sorted Matrix : " + str(res))
