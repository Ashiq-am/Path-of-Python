# Python3 code to demonstrate working of
# Cumulative Nested Tuple Column Product
# using zip() + nested generator expression

# initialize tuples
test_tup1 = ((1, 3), (4, 5), (2, 9), (1, 10))
test_tup2 = ((6, 7), (3, 9), (1, 1), (7, 3))

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Cumulative Nested Tuple Column Product
# using zip() + nested generator expression
res = tuple(tuple(a * b for a, b in zip(tup1, tup2))\
	for tup1, tup2 in zip(test_tup1, test_tup2))

# printing result
print("The resultant tuple after product : " + str(res))
