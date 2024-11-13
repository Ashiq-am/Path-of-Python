# Python3 code to demonstrate working of
# Test for Even values dictionary values lists
# Using all() + dictionary comprehension

# initializing dictionary
test_dict = {"Gfg" : [6, 7, 3],
			"is" : [8, 10, 12, 16],
			"Best" : [10, 16, 14, 6]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using all to check for all even elements
res = {sub : all(ele % 2 == 0 for ele in test_dict[sub]) for sub in test_dict}

# printing result
print("The computed dictionary : " + str(res))
