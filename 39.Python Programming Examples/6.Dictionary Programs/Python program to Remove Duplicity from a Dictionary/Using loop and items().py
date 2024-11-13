# initializing dictionary
test_dict = {'gfg': ['gfg', 'is', 'best'],
			'best': ['gfg'],
			'apple': ['good']}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

res = dict()
for key, val in test_dict.items():

	flag = True
	for key1, val1 in res.items():

		# filtering value from memoised values
		if key in val1:
			flag = False
	if flag:
		res[key] = val

# printing result
print("The filtered dictionary : " + str(res))
