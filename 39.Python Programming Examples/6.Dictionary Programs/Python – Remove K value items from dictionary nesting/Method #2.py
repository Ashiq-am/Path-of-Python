# Python3 code to demonstrate working of
# Remove K value items from dictionary nestings
# Using recursion + loop (For multiple nesting)

res = []

# helper function to solve problem
def hlper_fnc(test_dict):
	for key in test_dict:
		if type(test_dict[key]) == dict:
			hlper_fnc(test_dict[key])
		else:
			if test_dict[key] != K:
				res.append({key : test_dict[key]})

# initializing dictionary
test_dict = {"Gfg" : {"a" : 5, "b" : 8, "c" : 9},
			"is" : {"f" : 8, "l" : { "j" : 8, "k" : 10}},
			"Best" : {"i" : {"k" : { "o" : 8}}}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 8

# computing result
hlper_fnc(test_dict)

# printing result
print("The dictionary after value removal : " + str(res))
