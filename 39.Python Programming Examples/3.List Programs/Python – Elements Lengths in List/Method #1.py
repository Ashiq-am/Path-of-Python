# Python3 code to demonstrate working of
# Elements Lengths in List
# Using loop

# initializing list
test_list = ['GFG', (4, 5, 6), 17, [5, 6, 7, 8], 'Best']

# printing original list
print("The original list is : " + str(test_list))

# Elements Lengths in List
# Using loop
res = []
for ele in test_list:
	count = 0
	if type(ele) == int:
		res.append(1)
	else :
		for sub in ele:
			count = count + 1
		res.append(count)

# printing result
print("The element sizes in order are : " + str(res))
