# Python3 code to demonstrate working of
# Test if element is dictionary value
# Using loops

# initializing dictionary
test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Test if element is dictionary value
# Using loops
res = False
for key in test_dict:
	if(test_dict[key] == 3):
		res = True
		break

# printing result
print("Is 3 present in dictionary : " + str(res))
