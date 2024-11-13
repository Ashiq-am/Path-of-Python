# Python3 code to demonstrate working of
# Data type frequency in tuple
# Using loop + isinstance()

# initializing tuples
test_tuple = (5, 'Gfg', 2, 8.8, 1.2, 'is')

# printing original tuple
print("The original tuple : " + str(test_tuple))

# initializing data type
data_type = float

# Data type frequency in tuple
# Using loop + isinstance()
count = 0
for ele in test_tuple:
	if isinstance(ele, float):
		count = count + 1

# printing result
print("The data type frequency : " + str(count))
