# Python3 code to demonstrate
# accessing last element of list
# using [] operator

# initializing list
test_list = [1, 4, 5, 6, 3, 5]

# printing original list
print ("The original list is : " + str(test_list))

# using len - 1 index to print last list element
print ("The last element using [ len -1 ] is : "
		+ str(test_list[len(test_list) -1]))

# using -1 index to print last list element
print ("The last element using [ -1 ] is : "
					+ str(test_list[-1]))
