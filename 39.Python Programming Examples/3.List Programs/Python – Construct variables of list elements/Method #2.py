# Python3 code to demonstrate
# Construct variables of list elements
# using globals() + loop

# Initializing lists
test_list1 = ['gfg', 'is', 'best']
test_list2 = [1, 2, 3]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Construct variables of list elements
# using globals() + loop
for var, val in zip(test_list1, test_list2):
	globals()[var] = val

# printing result
print ("Variable value 1 : " + str(gfg))
print ("Variable value 2 : " + str(best))
