# Python3 code to demonstrate
# range deletion of elements
# using del + sorted()

# initializing list
test_list = [3, 5, 6, 7, 2, 10]

# initializing indices
indices_list = [1, 4, 2]

# printing the original list
print ("The original list is : " + str(test_list))

# printing the indices list
print ("The indices list is : " + str(indices_list))

# using del + sorted()
# range deletion of elements
for i in sorted(indices_list, reverse = True):
	del test_list[i]

# printing result
print ("The modified deleted list is : " + str(test_list))
