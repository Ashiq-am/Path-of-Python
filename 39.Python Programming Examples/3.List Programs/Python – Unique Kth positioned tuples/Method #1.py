# Python3 code to demonstrate working of
# Unique Kth index tuples
# Using map() + next() + lambda

# initializing list
test_list = [(5, 6, 8), (4, 2, 7), (1, 2, 3), (9, 6, 5)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# Unique Kth index tuples
# Using map() + next() + lambda
res = [*map(lambda ele: next(tup for tup in test_list if tup[K - 1] == ele),
	{tup[K - 1] for tup in test_list})]

# printing result
print("The extracted elements : " + str(res))
