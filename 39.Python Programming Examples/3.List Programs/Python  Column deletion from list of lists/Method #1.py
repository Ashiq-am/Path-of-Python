# Python3 code to demonstrate
# deleting columns of list of lists
# using del + loop

# initializing list
test_list = [[4, 5, 6, 8],
			[2, 7, 10, 9],
			[12, 16, 18, 20]]

# printing original list
print ("The original list is : " + str(test_list))

# using del + loop
# deleting column element of row
for j in test_list:
	del j[1]

# printing result
print ("The modified mesh after column deletion : " + str(test_list))
