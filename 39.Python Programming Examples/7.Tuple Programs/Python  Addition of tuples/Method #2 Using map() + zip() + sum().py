# Python3 code to demonstrate working of
# Addition of tuples
# using map() + zip() + sum()

# initialize tuples
test_tup1 = (10, 4, 5)
test_tup2 = (2, 5, 18)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Addition of tuples
# using map() + zip() + sum()
res = tuple(map(sum, zip(test_tup1, test_tup2)))

# printing result
print("Resultant tuple after addition : " + str(res))
