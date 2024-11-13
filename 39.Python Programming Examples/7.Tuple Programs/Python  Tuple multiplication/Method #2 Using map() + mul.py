# Python3 code to demonstrate working of
# Tuple multiplication
# using map() + mul
from operator import mul

# initialize tuples
test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Tuple multiplication
# using map() + mul
res = tuple(map(mul, test_tup1, test_tup2))

# printing result
print("The multiplied tuple : " + str(res))
