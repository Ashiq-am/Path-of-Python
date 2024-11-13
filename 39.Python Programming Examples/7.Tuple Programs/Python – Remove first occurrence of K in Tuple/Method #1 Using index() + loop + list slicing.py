# Python3 code to demonstrate working of
# Remove first occurrence of K in Tuple
# Using index() + loop + list slicing

# initializing tuples
test_tuple = (5, 6, 4, 4, 7, 8, 4)

# printing original tuple
print("The original tuple : " + str(test_tuple))

# initializing K
K = 4

# Remove first occurrence of K in Tuple
# Using index() + loop + list slicing
try:
	idx = test_tuple.index(K)
	res = test_tuple[:idx] + test_tuple[idx + 1:]
except ValueError:
	res = test_tuple

# printing result
print("Tuple after element removal : " + str(res))
