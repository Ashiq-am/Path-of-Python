# Python3 code to demonstrate working of
# Test for empty Nested Records
# Using recursion + all() + isinstance

# Helper function
def hlper_fnc(test_dict):
	if isinstance(test_dict, dict):
		return all(hlper_fnc(sub) for _, sub in test_dict.items())
	if isinstance(test_dict, list):
		return all(hlper_fnc(sub) for sub in test_dict)
	return False

# initializing dictionary
test_dict = {'Gfg': [], 'is': { 'best': [], 'for': {} }, 'geeks': {}}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Test for empty Nested Records
# Using recursion + all() + isinstance
res = hlper_fnc(test_dict)

# printing result
print("Is dictionary without data ? : " + str(res))
