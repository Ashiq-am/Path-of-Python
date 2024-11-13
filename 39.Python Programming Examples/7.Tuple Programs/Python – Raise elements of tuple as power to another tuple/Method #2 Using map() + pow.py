# Python3 code to demonstrate working of
# Tuple exponentiation
# using map() + pow
from operator import pow

# initialize tuples
test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Tuple exponentiation
# using map() + pow
res = tuple(map(pow, test_tup1, test_tup2))

# printing result
print("The exponentiated tuple : " + str(res))
