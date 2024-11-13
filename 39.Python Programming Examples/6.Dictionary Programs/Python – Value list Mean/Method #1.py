# Python3 code to demonstrate working of
# Value list mean
# Using loop + sum() + len()

# initializing dictionary
test_dict = {'Gfg' : [6, 7, 5, 4], 'is' : [10, 11, 2, 1], 'best' : [12, 1, 2]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Value list mean
# Using loop + sum() + len()
res = dict()
for key in test_dict:
	res[key] = sum(test_dict[key]) / len(test_dict[key])

# printing result
print("The dictionary average is : " + str(res))
