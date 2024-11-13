# Python3 code to demonstrate
# to test all elements in list are unique
# using set() + len()

# initializing list
test_list = [1, 3, 4, 6, 7]

# printing original list
print ("The original list is : " + str(test_list))

flag = 0

# using set() + len()
# to check all unique list elements
flag = len(set(test_list)) == len(test_list)


# printing result
if(flag) :
	print ("List contains all unique elements")
else :
	print ("List contains does not contains all unique elements")
