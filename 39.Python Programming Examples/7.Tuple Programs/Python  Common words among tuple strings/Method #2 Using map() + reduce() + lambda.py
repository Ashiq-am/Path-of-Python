# Python3 code to demonstrate working of
# Common words among tuple strings
# Using map() + reduce() + lambda

# Initializing tuple
test_tup = ('gfg is best', 'gfg is for geeks', 'gfg is for all')

# printing original tuple
print("The original tuple is : " + str(test_tup))

# Common words among tuple strings
# Using map() + reduce() + lambda
res = ", ".join(reduce(lambda i, j : i & j,
				map(lambda x: set(x.split()), test_tup)))

# printing result
print("Common words among tuple are : " + res)
