# Python3 code to demonstrate working of
# All possible items combination dictionary
# Using remove() + loop + update()

# initializing Dictionary
test_dict = {'gfg' : [1, 3], 'is' : [5, 6], 'best' : [4, 7]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# All possible items combination dictionary
# Using remove() + loop + update()
res = {}
for key, val in test_dict.items():
	for ele in val:
		temp = val[:]
		temp.remove(ele)
		res.update({ele: [key] + temp})
test_dict.update(res)

# printing result
print("The all possible items dictionary : " + str(test_dict))
