# Python3 code to demonstrate working of
# Dissimilar elements in tuples
# Using set() + "^" operator

# initialize tuples
test_tup1 = (3, 4, 5, 6)
test_tup2 = (5, 7, 4, 10)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Dissimilar elements in tuples
# Using set() + "^" operator
res = tuple(set(test_tup1) ^ set(test_tup2))

# printing result
print("The Dissimilar elements from tuples are : " + str(res))
