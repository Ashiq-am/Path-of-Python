# Python3 code to demonstrate working of
# Consecutive element concatenation in Tuple
# using zip() + generator expression + tuple

# initialize tuple
test_tup = ("GFG ", "IS ", "BEST ", "FOR ", "ALL ", "GEEKS")

# printing original tuple
print("The original tuple : " + str(test_tup))

# Consecutive element concatenation in Tuple
# using zip() + generator expression + tuple
res = tuple(i + j for i, j in zip(test_tup, test_tup[1:]))

# printing result
print("Resultant tuple after consecutive concatenation : " + str(res))
