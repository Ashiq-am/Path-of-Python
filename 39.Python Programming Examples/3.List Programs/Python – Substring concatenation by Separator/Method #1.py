# Python3 code to demonstrate working of
# Substring concatenation by Separator
# Using loop

# initializing list
test_list = ['gfg', 'is', '*', 'best', '*', 'for', 'geeks']

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = '*'

# Substring concatenation by Separator
# Using loop
res = []
temp = ''
for sub in test_list:
	if sub != '*':
		temp += sub
	else:
		res.append(temp)
		temp = ''
if temp:
	res.append(temp)

# printing result
print("The list after String concatenation : " + str(res))
