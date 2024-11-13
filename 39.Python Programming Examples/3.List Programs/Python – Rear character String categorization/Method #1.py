# Python3 code to demonstrate
# Rear character String categorization
# using next() + lambda + loop

# initializing list
test_list = ['an', 'apple', 'geek', 'for', 'greek', 'free']

# printing original list
print("The original list : " + str(test_list))

# using next() + lambda + loop
# Rear character String categorization
util_func = lambda x, y: x[len(x) - 1] == y[len(y) - 1]
res = []
for sub in test_list:
	ele = next((x for x in res if util_func(sub, x[len(x) - 1])), [])
	if ele == []:
		res.append(ele)
	ele.append(sub)

# print result
print("The list after Categorization : " + str(res))
