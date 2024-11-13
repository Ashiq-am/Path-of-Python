# Python3 code to demonstrate
# Difference of List keeping duplicates
# using loop

# Initializing lists
test_list1 = [4, 5, 7, 4, 3]
test_list2 = [7, 3, 4]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Difference of List keeping duplicates
# using loop
for ele in test_list2:
	for sub in test_list1:
		if ele == sub:
			test_list1.remove(sub)
			break

# printing result
print ("List after performing difference : " + str(test_list1))
