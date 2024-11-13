# Python3 code to demonstrate
# Truth values deletion in List
# using naive method

# initializing list
test_list = [1, None, 4, None, False, 5, 8, False]

# printing original list
print ("The original list is : " + str(test_list))

# using naive method
# Truth values deletion in List
res = []
for val in test_list:
	if not val:
		res.append(val)

# printing result
print ("List after removal of Truth values : " + str(res))
