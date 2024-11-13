# Python3 code to demonstrate working of
# Remove K valued key from Nested Dictionary
# Using dictionary comprehension + isinstance() + lamda

# initializing dictionary
test_dict = {'gfg' : {'best' : 4, 'good' : 5},
			'is' : {'better' : 6, 'educational' : 4},
			'CS' : {'priceless' : 6}}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing rem_val
rem_val = 6

# Remove K valued key from Nested Dictionary
# Using dictionary comprehension + isinstance() + lamda
fnc = lambda sub: { key1: fnc(val1) if isinstance(val1, dict) else val1
	for key1, val1 in sub.items() if val1 != rem_val}
res = fnc(test_dict)

# printing result
print("Dictionary after removal : " + str(res))
