# Python3 code to demonstrate
# Initial Character Case Categorization
# using next() + lambda + loop

# initializing list
test_list = ['an', 'a', 'geek', 'for', 'g', 'free']

# printing original list
print("The original list : " + str(test_list))

# using next() + lambda + loop
# Initial Character Case Categorization
util_func = lambda x, y: x[0] == y[0]
res = []
for sub in test_list:
	ele = next((x for x in res if util_func(sub, x[0])), [])
	if ele == []:
		res.append(ele)
	ele.append(sub)

# print result
print("The list after Categorization : " + str(res))
