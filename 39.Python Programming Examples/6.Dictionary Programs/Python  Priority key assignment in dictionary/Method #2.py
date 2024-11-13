# Python3 code to demonstrate working of
# Priority key assignment in dictionary
# Using nested get()

# Initialize dictionary
test_dict = {'gfg' : 6, 'is' : 4, 'for' : 2, 'CS' : 10}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize priority keys
prio_list = ['best', 'gfg', 'CS']

# Using nested get()
# Priority key assignment in dictionary
res = test_dict.get(prio_list[0], test_dict.get(prio_list[1],
								test_dict.get(prio_list[2])))

# printing result
print("The variable value after assignment : " + str(res))
