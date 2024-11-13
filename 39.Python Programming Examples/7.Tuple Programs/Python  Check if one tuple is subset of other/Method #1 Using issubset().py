# Python3 code to demonstrate working of
# Check if one tuple is subset of other
# using issubset()

# initialize tuples
test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 10)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Check if one tuple is subset of other
# using issubset()
res = set(test_tup2).issubset(test_tup1)

# printing result
print("Is 2nd tuple subset of 1st ? : " + str(res))
