# Python3 code to demonstrate working of
# Paired Existance in Records
# Using generator expression

# initializing list
test_list = [('Gfg', 'is', 'Best'),
			('Gfg', 'is', 'good'),
			('CS', 'is', 'good')]

# printing original list
print("The original list is : " + str(test_list))

# initializing Pairs
pairs = ('Gfg', 'Best')

# Paired Existance in Records
# Using generator expression
res = []
for sub in test_list:
	if ((pairs[0] in sub and pairs[1] in sub) or (
		pairs[0] not in sub and pairs[1] not in sub)):
		res.append(sub)

# printing result
print("The resultant records : " + str(res))
