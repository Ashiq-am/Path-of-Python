# Python3 code to demonstrate working of
# Detect loop in Dictionaries
# Using any() + loop

# initializing dictionaries
test_dict1 = {7 : [1, 2], 8 : [1, 4], 9 : [4, 2]}
test_dict2 = {2 : [1, 7], 10 : [1, 6], 11 : [24, 20]}

# printing original dictionaries
print("The original dictionary 1 is : " + str(test_dict1))
print("The original dictionary 2 is : " + str(test_dict2))

# Detect loop in Dictionaries
# Using any() + loop
res = False
for key, val in test_dict1.items():
	if any([vl in test_dict2 and key in test_dict2[vl] for vl in val]):
		res = True

# printing result
print("Does dictionaries contain loop : " + str(res))
