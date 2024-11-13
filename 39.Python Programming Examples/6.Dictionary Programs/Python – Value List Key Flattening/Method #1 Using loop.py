# Python3 code to demonstrate working of
# Value List Key Flattening
# Using loop

# initializing dictionary
test_dict = {'gfg' : [4, 5, 7], 'best' : [10, 12]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Value List Key Flattening
# Using loop
res = []
for key, vals in test_dict.items():
	for ele in vals:
		res.append({"key": key, "value": ele})

# printing result
print("The flattened dictionary : " + str(res))
