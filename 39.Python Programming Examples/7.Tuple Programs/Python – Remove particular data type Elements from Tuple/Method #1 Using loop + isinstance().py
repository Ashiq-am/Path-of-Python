# Python3 code to demonstrate working of
# Remove particular data type Elements from Tuple
# Using loop + isinstance()

# initializing tuple
test_tuple = (4, 5, 'Gfg', 7.7, 'Best')

# printing original tuple
print("The original tuple : " + str(test_tuple))

# initializing data type
data_type = int

# Remove particular data type Elements from Tuple
# Using loop + isinstance()
res = []
for ele in test_tuple:
	if not isinstance(ele, data_type):
		res.append(ele)

# printing result
print("The filtered tuple : " + str(res))
