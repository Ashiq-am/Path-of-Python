# Python3 code to demonstrate working of
# Similar front and rear elements
# Using loop

# initialize list
test_list = ['gfg', 'is', 'best', 'treat']

# printing original list
print("The original list : " + str(test_list))

# Similar front and rear elements
# Using loop
count = 0
for ele in test_list:
	if ele[0] == ele[-1]:
		count = count + 1

# printing result
print("Total Strings with similar front and rear elements : " + str(count))
