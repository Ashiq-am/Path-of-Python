# Python3 code to demonstrate working of
# Get tuple element data types
# Using map() + type()

# Initializing tuple
test_tup = ('gfg', 1, ['is', 'best'])

# printing original tuple
print("The original tuple is : " + str(test_tup))

# Get tuple element data types
# Using map() + type()
res = list(map(type, test_tup))

# printing result
print("The data types of tuple in order are : " + str(res))
