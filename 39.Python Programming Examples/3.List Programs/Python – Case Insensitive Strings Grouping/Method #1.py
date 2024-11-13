# Python3 code to demonstrate
# Case Insensitive Strings Grouping
# using next() + lambda + loop

# initializing list
test_list = ['man', 'a', 'gEek', 'for', 'GEEK', 'FoR']

# printing original list
print("The original list : " + str(test_list))

# using next() + lambda + loop
# Case Insensitive Strings Grouping
util_func = lambda x, y: str.lower(x) == str.lower(y)
res = []
for sub in test_list:
	ele = next((x for x in res if util_func(sub, x[0])), [])
	if ele == []:
		res.append(ele)
	ele.append(sub)

# print result
print("The list after Categorization : " + str(res))
