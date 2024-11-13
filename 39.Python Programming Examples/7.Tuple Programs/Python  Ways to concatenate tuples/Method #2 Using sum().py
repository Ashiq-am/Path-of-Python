# Python3 code to demonstrate working of
# Ways to concatenate tuples
# using sum()

# initialize tuples
test_tup1 = (1, 3, 5)
test_tup2 = (4, 6)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Ways to concatenate tuples
# using sum()
res = sum((test_tup1, test_tup2), ())

# printing result
print("The tuple after concatenation is : " + str(res))
