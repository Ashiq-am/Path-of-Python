# Python 3 code to demonstrate working of
# Tuple elements inversions
# Using map() + list() + tuple() + operator.invert
from operator import invert

# initializing tup
test_tup = (7, 8, 9, 1, 10, 7)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# Tuple elements inversions
# Using map() + list() + tuple() + operator.invert
res = tuple(list(map(invert, list(test_tup))))

# printing result
print("The Bitwise Inversions of tuple elements are : " + str(res))
