# Python3 code to demonstrate working of
# Convert Values into proportions
# Using sum() + loop

# initializing dictionary
test_dict = { 'gfg' : 10, 'is' : 15, 'best' : 20 }

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert Values into proportions
# Using sum() + loop
temp = sum(test_dict.values())
for key, val in test_dict.items():
	test_dict[key] = val / temp

# printing result
print("The proportions divided values : " + str(test_dict))
