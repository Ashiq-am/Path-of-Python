# Python3 code to demonstrate working of
# Test Boolean Value of Dictionary
# Using loop

# initializing dictionary
test_dict = {'gfg' : True, 'is' : False, 'best' : True}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Test Boolean Value of Dictionary
# Using loop
res = True
for ele in test_dict:
	if not test_dict[ele]:
		res = False
		break

# printing result
print("Is Dictionary True ? : " + str(res))
