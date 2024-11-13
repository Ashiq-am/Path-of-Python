# Python3 code to demonstrate
# removing None values in list
# using naive method

# initializing list
test_list = [1, None, 4, None, None, 5, 8, None]

# printing original list
print ("The original list is : " + str(test_list))

# using naive method
# to remove None values in list
res = []
for val in test_list:
	if val != None :
		res.append(val)

# printing result
print ("List after removal of None values : " + str(res))
