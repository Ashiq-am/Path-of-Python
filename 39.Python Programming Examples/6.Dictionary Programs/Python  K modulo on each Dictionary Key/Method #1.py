# Python3 code to demonstrate working of
# K modulo on each Dictionary Key
# Using loop

# Initialize dictionary
test_dict = {'gfg' : 6, 'is' : 4, 'best' : 7}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing K
K = 4

# Using loop
# K modulo on each Dictionary Key
for key in test_dict:
	test_dict[key] %= 4

# printing result
print("The dictionary after mod K each key's value : " + str(test_dict))
