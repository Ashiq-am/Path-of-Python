# Python3 code to demonstrate working of
# Unique Value Lists Dictionaries
# Using loop

# initializing lists
test_list = [{'Gfg': [2, 3], 'is' : [7, 8], 'best' : [10]},
			{'Gfg': [2, 3], 'is' : [7], 'best' : [10]},
			{'Gfg': [2, 3], 'is' : [7, 8], 'best' : [10]}]

# printing original list
print("The original list : " + str(test_list))

# Using loop to iterate through elements
# result array to also keep track of already occurred elements
res = []
for sub in test_list:
	if sub not in res:
		res.append(sub)

# printing result
print("List after duplicates removal : " + str(res))
