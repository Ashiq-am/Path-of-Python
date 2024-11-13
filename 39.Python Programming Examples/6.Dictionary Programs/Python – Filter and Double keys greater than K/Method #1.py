# Python3 code to demonstrate working of
# Filter and Double keys greater than K
# Using loop

# initializing dictionary
test_dict = {'Gfg' : 4, 'is' : 2, 'best': 3, 'for' : 6, 'geeks' : 1}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing K
K = 2

# Filter and Double keys greater than K
# Using loop
res = dict()
for key, val in test_dict.items():
	if val > K:
		res[key] = val * 2

# printing result
print("The filtred dictionary : " + str(res))
