# Python3 code to demonstrate working of
# Check order specific data type in tuple
# Using map() + type() + isinstance()

# Initializing tuple
test_tup = ('gfg', ['is', 'best'], 1)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# data type order list
data_list = [str, list, int]

# Check order specific data type in tuple
# Using map() + type() + isinstance()
res = isinstance(test_tup, tuple) and list(map(type, test_tup)) == data_list

# printing result
print("Does all the instances match required data types in order ? : " + str(res))
