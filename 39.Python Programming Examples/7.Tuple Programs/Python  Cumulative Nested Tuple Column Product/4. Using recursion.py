# function to perform task
def tup_prod(tup1, tup2):
	if isinstance(tup1, (list, tuple)) and isinstance(tup2, (list, tuple)):
		res = []
		for x, y in zip(tup1, tup2):
			res.append(tup_prod(x, y))
		return tuple(res)
	return tup1 * tup2

# initialize tuples
test_tup1 = ((1, 3), (4, 5), (2, 9), (1, 10))
test_tup2 = ((6, 7), (3, 9), (1, 1), (7, 3))

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Cumulative Nested Tuple Column Product
# using recursion
res = tup_prod(test_tup1, test_tup2)

# printing result
print("The resultant tuple after product : " + str(res))
