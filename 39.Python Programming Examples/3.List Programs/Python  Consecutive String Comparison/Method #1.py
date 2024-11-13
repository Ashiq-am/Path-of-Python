# Python3 code to demonstrate working of
# Consecutive String Comparison
# using zip() + loop

# initialize list
test_list = ['gfg', 'gfg', 'is', 'best', 'best', 'for', 'geeks', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# Consecutive String Comparison
# using zip() + loop
res = []
for i, j in zip(test_list, test_list[1: ]):
	if i == j:
		res.append(i)

# printing result
print("List of Consecutive similar elements : " + str(res))
