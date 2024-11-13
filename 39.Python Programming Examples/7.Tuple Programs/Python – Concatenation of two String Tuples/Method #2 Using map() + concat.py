# Python3 code to demonstrate working of
# Tuple String concatenation
# using map() + concat
from operator import concat

# initialize tuples
test_tup1 = ("Manjeet", "Nikhil", "Akshat")
test_tup2 = (" Singh", " Meherwal", " Garg")

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Tuple String concatenation
# using map() + concat
res = tuple(map(concat, test_tup1, test_tup2))

# printing result
print("The concatenated tuple : " + str(res))
