# Python3 code to demonstrate working of
# Even values update in dictionary
# Using loop

# Initialize dictionary
test_dict = {'gfg' : 6, 'is' : 4, 'best' : 7}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Using loop
# Even values update in dictionary
for key in test_dict:
	if test_dict[key] % 2 == 0:
		test_dict[key] *= 3

# printing result
print("The dictionary after triple even key's value : " + str(test_dict))
