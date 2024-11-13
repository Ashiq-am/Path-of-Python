# Python3 code to demonstrate working of
# Convert Value list elements to List records
# Using loop + enumerate()

# initializing dictionary
test_dict = {'gfg' : [4, 5], 'is' : [8], 'best' : [10]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Convert Value list elements to List records
# Using loop + enumerate()
for ele in test_dict.values():
	for idx, val in enumerate(ele):
		ele[idx] = {val: []}

# printing result
print("The converted dictionary is : " + str(test_dict))
