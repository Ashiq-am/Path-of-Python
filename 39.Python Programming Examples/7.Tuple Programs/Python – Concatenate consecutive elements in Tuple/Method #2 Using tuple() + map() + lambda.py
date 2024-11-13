# Python3 code to demonstrate working of
# Consecutive element concatenation in Tuple
# using tuple() + map() + lambda

# initialize tuple
test_tup = ("GFG ", "IS ", "BEST ", "FOR ", "ALL ", "GEEKS")

# printing original tuple
print("The original tuple : " + str(test_tup))

# Consecutive element concatenation in Tuple
# using tuple() + map() + lambda
res = tuple(map(lambda i, j : i + j, test_tup[: -1], test_tup[1: ]))

# printing result
print("Resultant tuple after consecutive concatenation : " + str(res))
