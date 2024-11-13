# Python3 code to demonstrate working of
# Non-None dictionary Keys
# Using loop

# initializing dictionary
test_dict = {'Gfg' : 1, 'for' : 2, 'CS' : None}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using loop
# Non-None dictionary Keys
res = []
for ele in test_dict:
	if test_dict[ele] is not None :
		res.append(ele)

# printing result
print("Non-None keys list : " + str(res))
