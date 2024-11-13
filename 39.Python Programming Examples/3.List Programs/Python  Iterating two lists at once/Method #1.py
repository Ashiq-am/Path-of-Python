# Python3 code to demonstrate working of
# Iterating two lists at once
# using loop + "+" operator

# initializing lists
test_list1 = [4, 5, 3, 6, 2]
test_list2 = [7, 9, 10, 0]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Iterating two lists at once
# using loop + "+" operator
# printing result
print("The paired list contents are : ")
for ele in test_list1 + test_list2:
	print(ele, end =" ")
