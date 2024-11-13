# Python3 code to demonstrate working of
# Value's Key association
# Using loop + items()

# initializing dictionary
test_dict = {'gfg' : [4, 5], 'is' : [8], 'best' : [10, 12]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing value list
val_list = [5, 10]

# Value's Key association
# Using loop + items()
temp = {}
for key, vals in test_dict.items():
	for val in vals:
		temp[val] = key
res = [temp[ele] for ele in val_list]

# printing result
print("The keys mapped to " + str(val_list) + " are : " + str(res))
