# Python3 code to demonstrate working of
# Remove Disjoint Tuple keys from Dictionary
# Using loop

# initializing dictionary
test_dict = {('Gfg', 3) : 4, ('is', 6) : 2, ('best', 10) : 3, ('for', 9) : 'geeks'}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing List
rem_list = [9, 'is']

# Remove Disjoint Tuple keys from Dictionary
# Using loop
res = dict()
for idx in test_dict:
	if idx[0] not in rem_list and idx[1] not in rem_list:
		res[idx] = test_dict[idx]

# printing result
print("Dictionary after removal : " + str(res))
