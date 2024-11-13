# Python3 code to demonstrate working of
# Detect loop in Dictionaries
# Using loop

# initializing dictionaries
test_dict1 = {7 : [1, 2], 8 : [1, 4], 9 : [4, 2]}
test_dict2 = {2 : [1, 7], 10 : [1, 6], 11 : [24, 20]}

# printing original dictionaries
print("The original dictionary 1 is : " + str(test_dict1))
print("The original dictionary 2 is : " + str(test_dict2))

# Detect loop in Dictionaries
# Using loop
res = False
for idx1 in test_dict1.values():
	temp1 = (idx for idx in idx1 if idx in test_dict2)
	for idx in temp1:
		for idx2 in test_dict2[idx]:
			if idx2 in test_dict1:
				res = True

# printing result
print("Does dictionaries contain loop : " + str(res))
