# Python3 code to demonstrate working of
# Comparing tuples
# using all() + lambda + map()

# initialize tuples
test_tup1 = (10, 4, 5)
test_tup2 = (13, 5, 18)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Comparing tuples
# using all() + lambda + map()
res = all(map(lambda i, j: i < j, test_tup1, test_tup2))

# printing result
print("Are all elements in second tuple greater than first ? : " + str(res))
