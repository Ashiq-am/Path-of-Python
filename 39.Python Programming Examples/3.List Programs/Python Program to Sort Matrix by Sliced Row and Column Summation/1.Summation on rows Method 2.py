# initializing list
test_list = [[1, 4, 3, 1, 3], [3, 4, 5, 2, 4],
			[23, 5, 5, 3], [2, 3, 5, 1, 6]]

# printing original list
print("The original list is : " + str(test_list))

# initializing range
i, j = 1, 3

# performing sort using sorted()
# filter util. using lambda fnc.
res = sorted(test_list, key=lambda row: sum(row[i:j]))

# printing result
print("Sorted List : " + str(res))
