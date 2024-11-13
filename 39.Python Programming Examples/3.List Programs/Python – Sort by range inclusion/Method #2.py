# Python3 code to demonstrate working of
# Sort by range inclusion
# Using sorted() + lambda + sum()

# initializing list
test_list = [[(1, 5), (6, 10), (10, 15)], [(3, 16)], [
	(2, 4), (6, 8), (9, 14)], [(1, 3), (9, 13)]]

# printing original list
print("The original list is : " + str(test_list))

# initializing range
i, j = 2, 15

# sorting using sorted() + lambda
res = sorted(test_list, key=lambda row: sum(
	[abs(sub[1] - sub[0]) for sub in row if sub[0] > i and sub[0] < j and sub[1] > i and sub[1] < j]))

# printing result
print("Sorted List : " + str(res))
