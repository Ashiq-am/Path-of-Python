# Python3 code to demonstrate
# Categorize by string size
# using next() + lambda + loop

# initializing list
test_list = ['man', 'a', 'geek', 'for', 'b', 'free']

# printing original list
print("The original list : " + str(test_list))

# using next() + lambda + loop
# Categorize by string size
util_func = lambda x, y: len(x) == len(y)
res = []
for sub in test_list:
	ele = next((x for x in res if util_func(sub, x[0])), [])
	if ele == []:
		res.append(ele)
	ele.append(sub)

# print result
print("The list after Categorization : " + str(res))
