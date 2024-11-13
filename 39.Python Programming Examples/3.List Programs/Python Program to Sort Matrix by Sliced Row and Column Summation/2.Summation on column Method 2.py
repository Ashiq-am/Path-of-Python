# initializing list
test_list = [[1, 4, 3, 1], [3, 4, 5, 2],
			[23, 5, 5, 3], [2, 3, 5, 1]]

# printing original list
print("The original list is : " + str(test_list))

# initializing range
i, j = 1, 3

# transposing matrix
test_list = zip(*test_list)

# performing sort using sorted()
# filter util. using lambda fnc.
res = sorted(test_list, key=lambda row: sum(row[i:j]))

# performing transpose again to get result.
res = zip(*res)

# converting list of tuples to list of lists
res = [list(sub) for sub in res]

# printing result
print("Sorted List Columnwise : " + str(list(res)))
