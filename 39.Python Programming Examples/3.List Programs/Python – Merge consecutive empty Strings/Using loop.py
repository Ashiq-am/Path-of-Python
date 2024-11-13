# Python3 code to demonstrate
# Merge consecutive empty Strings
# using loop

# Initializing list
test_list = ['Gfg', '', '', '', 'is', '', '', 'best', '']

# printing original list
print("The original list is : " + str(test_list))

# Merge consecutive empty Strings
# using loop
count = 0
res = []
for ele in test_list:
	if ele =='':
		count += 1
		if (count % 2)== 0:
			res.append('')
			count = 0
	else:
		res.append(ele)

# printing result
print ("List after removal of consecutive empty strings : " + str(res))
