# Python3 code to demonstrate working of
# All possible items combination dictionary
# Using loop + set()

# initializing Dictionary
test_dict = {'gfg' : [1, 3], 'is' : [5, 6], 'best' : [4, 7]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# All possible items combination dictionary
# Using loop + set()
temp = [set([key]) | set(value) for key, value in test_dict.items() ]
res = {}
for sub in temp:
	for key in sub:
		res[key] = list(sub - set([key]))

# printing result
print("The all possible items dictionary : " + str(res))
