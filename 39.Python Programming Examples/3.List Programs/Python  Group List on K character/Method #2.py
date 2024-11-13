# Python3 code to demonstrate
# Group List on K character
# using loop

# initializing list
test_list = ['Geeks', 'M', 'for', 'M', 4, 5, 'M', 'Geeks', 'CS', 'M', 'Portal']

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 'M'

# using loop
# Group List on K character
temp = []
res = []
for ele in test_list:
	if ele == K:
		res.append(temp)
		temp = []
	else:
		temp.append(ele)
res.append(temp)

# print result
print("The list of sublist after separation : " + str(res))
