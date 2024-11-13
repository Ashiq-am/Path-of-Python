# Python3 code to demonstrate
# to test all elements in list are unique
# using naive method

# initializing list
test_list = [1, 3, 4, 6, 7]

# printing original list
print ("The original list is : " + str(test_list))

flag = 0

# using naive method
# to check all unique list elements
for i in range(len(test_list)):
		for i1 in range(len(test_list)):
			if i != i1:
				if test_list[i] == test_list[i1]:
					flag = 1


# printing result
if(not flag) :
	print ("List contains all unique elements")
else :
	print ("List contains does not contains all unique elements")
