# Python3 code to demonstrate working of
# Test if all values are K in dictionary
# Using loop

# Initialize dictionary
test_dict = {'gfg' : 8, 'is' : 8, 'best' : 8}

# Printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Initialize K
K = 8

# using loop
# Test if all values are K in dictionary
res = True
for key in test_dict:
	if test_dict[key] != K:
		res = False

# printing result
print("Does all keys have K value ? : " + str(res))
