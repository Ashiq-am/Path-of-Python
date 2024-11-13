# Python3 code to demonstrate working of
# Remove None Nested Records
# Using any() + dictionary comprehension

# initializing dictionary
test_dict = {'gfg' : {'a' : 1, 'b' : 2},
			'is' : {'d' : None, 'e' : None},
			'best' : {'g' : 1}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Remove None Nested Records
# Using any() + dictionary comprehension
res = {key: sub1 for key, sub1 in test_dict.items() if
	any(sub2 is not None for sub2 in sub1.values())}

# printing result
print("The dictionary after removal : " + str(res))
