# Python3 code to demonstrate working of
# Tuple elements inversions
# Using map() + list() + tuple() + lambda + "~" operator

# initializing tup
test_tup = (7, 8, 9, 1, 10, 7)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# Tuple elements inversions
# Using map() + list() + tuple() + lambda + "~" operator
res = tuple(list(map(lambda x: ~x, list(test_tup))))

# printing result
print("The Bitwise Inversions of tuple elements are : " + str(res))
