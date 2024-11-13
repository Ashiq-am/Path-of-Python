# Python3 code to demonstrate working of
# Tuple division
# using map() + floordiv
from operator import floordiv

# initialize tuples
test_tup1 = (10, 4, 6, 9)
test_tup2 = (5, 2, 3, 3)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Tuple division
# using map() + floordiv
res = tuple(map(floordiv, test_tup1, test_tup2))

# printing result
print("The divided tuple : " + str(res))
