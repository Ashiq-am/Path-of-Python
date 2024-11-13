# Python3 code to demonstrate working of
# Relative sorted order in Matrix
# using list comprehension + enumerate() + sort() + lambda

# initialize list
test_list = [[1, 3, 1], [4, 6], [7, 8, 10]]

# printing original list
print("The original list is : " + str(test_list))

# Relative sorted order in Matrix
# using list comprehension + enumerate() + sort() + lambda
res = [(i, j) for i, x in enumerate(test_list) for
	j, _ in enumerate(x)]
res.sort(key = lambda f: test_list[f[0]][f[1]])

# printing result
print("Sorted order of Matrix elements : " + str(res))
