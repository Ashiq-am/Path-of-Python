# Python3 code to demonstrate working of
# Value Dictionary from Record List
# Using zip() + iter()

# initializing list
test_list = [{1 : 'gfg', 2 : 'best'}, {3 : 'for', 4 : 'geeks'}]

# printing original list
print("The original list is : " + str(test_list))

# Value Dictionary from Record List
# Using zip() + iter()
res = dict()
for sub in test_list:
	itr = iter(sub.values())
	res.update(dict(zip(itr, itr)))

# printing result
print("The values dictionary is : " + str(res))
