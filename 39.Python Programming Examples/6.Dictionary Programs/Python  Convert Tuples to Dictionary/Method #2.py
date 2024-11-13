# Python3 code to demonstrate working of
# Convert Tuples to Dictionary
# Using zip() + dict()

# initializing tuples
test_tup1 = ('GFG', 'is', 'best')
test_tup2 = (1, 2, 3)

# printing original tuples
print("The original key tuple is : " + str(test_tup1))
print("The original value tuple is : " + str(test_tup2))

# Using zip() + dict()
# Convert Tuples to Dictionary
if len(test_tup1) == len(test_tup2):
	res = dict(zip(test_tup1, test_tup2))

# printing result
print("Dictionary constructed from tuples : " + str(res))
