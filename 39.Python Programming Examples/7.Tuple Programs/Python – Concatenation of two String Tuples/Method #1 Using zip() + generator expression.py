# Python3 code to demonstrate working of
# Tuple String concatenation
# using zip() + generator expression

# initialize tuples
test_tup1 = ("Manjeet", "Nikhil", "Akshat")
test_tup2 = (" Singh", " Meherwal", " Garg")

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Tuple String concatenation
# using zip() + generator expression
res = tuple(ele1 + ele2 for ele1, ele2 in zip(test_tup1, test_tup2))

# printing result
print("The concatenated tuple : " + str(res))
