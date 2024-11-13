# Python3 code to demonstrate working of
# Convert Tuple value list to List of tuples
# Using loop + * operator + items()

# initializing dictionary
test_dict = {'Gfg' : [(5, 6, 7), (1, 3), (6, )],
			'is' : [(5, 5, 2, 2, 6)],
			'best' :[(7, ), (9, 16)]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using items() to extract all the items of
# dictionary
res = []
for key, val in test_dict.items():
	for ele in val:
		res.append((key, *ele))

# printing result
print("The converted tuple list : " + str(res))
