# Python3 code to demonstrate working of
# Check order specific data type in tuple
# Using chained if and isinstance()

# Initializing tuple
test_tup = ('gfg', ['is', 'best'], 1)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# Check order specific data type in tuple
# Using chained if and isinstance()
res = isinstance(test_tup, tuple)\
	and isinstance(test_tup[0], str)\
	and isinstance(test_tup[1], list)\
	and isinstance(test_tup[2], int)

# printing result
print("Does all the instances match required data types in order ? : " + str(res))
