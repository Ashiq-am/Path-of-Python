# Python3 code to demonstrate working of
# Priority key assignment in dictionary
# Using loop

# Initialize dictionary
test_dict = {'gfg' : 6, 'is' : 4, 'for' : 2, 'CS' : 10}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize priority keys
prio_list = ['best', 'gfg', 'CS']

# Using loop
# Priority key assignment in dictionary
res = None
for key in test_dict:
	if key in prio_list :
		res = test_dict[key]
		break

# printing result
print("The variable value after assignment : " + str(res))
