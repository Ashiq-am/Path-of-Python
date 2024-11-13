# Python3 code to demonstrate working of
# Merge Similar Dictionaries in List
# Using loop + "**" operator

# initializing list
test_list = [{'gfg' : 1}, {'is' : 2}, {'best' : 3},
			{'gfg' : 5}, {'is' : 17}, {'best' : 14},
			{'gfg' : 7}, {'is' : 8}, {'best' : 10},]

# printing original list
print("The original list is : " + str(test_list))

# Merge Similar Dictionaries in List
# Using loop + "**" operator
res = [{}]
for sub in test_list:
	if list(sub)[0] not in res[-1]:
		res[-1] = {**res[-1], **sub}
	else:
		res.append(sub)

# printing result
print("The merged dictionaries : " + str(res))
