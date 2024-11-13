# Python3 code to demonstrate working of
# Remove List elements containing String character
# Using loop

# initializing list
test_list = ['567', '840', '649', '7342']

# initializing string
test_str = '1237'

# printing original list
print("The original list is : " + str(test_list))

# Remove List elements containing String character
# Using loop
res = []
for sub in test_list:
	flag = 0
	for ele in sub:
		if ele in test_str:
			flag = 1
	if not flag:
		res.append(sub)

# printing result
print("The list after removal : " + str(res))
