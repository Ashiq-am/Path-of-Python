# Python3 code to demonstrate
# List Strings frequency in Matrix
# using count() + loop

# Initializing lists
test_list1 = [['Gfg', 'is', 'best'], ['Gfg', 'is', 'for', 'CS'], ['Gfg', 'is', 'for', 'Geeks']]
test_list2 = ['Gfg', 'is', 'best']

# printing original list1
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# List Strings frequency in Matrix
# using count() + loop
res = []
for val in test_list1:
	res.append([val.count(ele) for ele in test_list2])

# printing result
print ("Frequency of strings in Matrix : " + str(res))
