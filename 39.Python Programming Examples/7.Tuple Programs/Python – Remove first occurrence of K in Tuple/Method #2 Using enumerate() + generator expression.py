# Python3 code to demonstrate working of
# Remove first occurrence of K in Tuple
# Using enumerate() + generator expression

# initializing tuples
test_tuple = (5, 6, 4, 4, 7, 8, 4)

# printing original tuple
print("The original tuple : " + str(test_tuple))

# initializing K
K = 4

# Remove first occurrence of K in Tuple
# Using enumerate() + generator expression
res = tuple(ele for idx, ele in enumerate(test_tuple) if idx != test_tuple.index(K))

# printing result
print("Tuple after element removal : " + str(res))
