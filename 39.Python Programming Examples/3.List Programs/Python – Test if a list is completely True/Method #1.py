# Python3 code to demonstrate
# Pure List Test
# using naive method

# initializing list
test_list = [True, True, True, True]

# printing original list
print ("The original list is : " + str(test_list))

flag = 0

# using naive method
# Pure List Test
for i in test_list :
	if not i :
		flag = 1
		break

# printing result
print ("Is List completely True ? : " + str(bool(not flag)))
