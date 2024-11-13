# Python3 code to demonstrate working of
# Index Maximum among Tuples
# using map() + lambda + max()

# initialize tuples
test_tup1 = (10, 4, 5)
test_tup2 = (2, 5, 18)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Index Maximum among Tuples
# using map() + lambda + max()
res = tuple(map(lambda i, j: max(i, j), test_tup1, test_tup2))

# printing result
print("Resultant tuple after maximization : " + str(res))
