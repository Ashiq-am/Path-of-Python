# Python3 code to demonstrate
# numeric string sorting
# using naive method

# initializing list
test_list = [ '4', '6', '7', '2', '1']

# printing original list
print ("The original list is : " + str(test_list))

# using naive method
# numeric string sorting
for i in range(0, len(test_list)) :
	test_list[i] = int(test_list[i])
test_list.sort()

# printing result
print ("The resultant sorted list : " + str(test_list))
