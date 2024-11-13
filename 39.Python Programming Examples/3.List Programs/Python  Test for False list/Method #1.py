# Python3 code to demonstrate
# to check for False list
# using naive method

# initializing list
test_list = [False, False, False, False]

# printing original list
print ("The original list is : " + str(test_list))

flag = 0

# using naive method
# to check for False list
for i in test_list :
	if i == True :
		flag = 1
		break

# printing result
print ("Is List completely false ? : " + str(bool(not flag)))
