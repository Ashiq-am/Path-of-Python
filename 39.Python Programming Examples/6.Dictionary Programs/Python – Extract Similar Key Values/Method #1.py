# Python3 code to demonstrate working of
# Extract Similar Key Values
# Using loop + sorted()

# initializing dictionary
test_dict = {'gfg': 5, 'ggf': 19, 'gffg': 9, 'gff': 3, 'fgg': 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing word
tst_wrd = 'fgg'

res = []
for key, val in test_dict.items():

	# sorted to get similar key order
	if ''.join(list(sorted(key))) == tst_wrd:
		res.append(val)

# printing result
print("The extracted keys : " + str(res))
