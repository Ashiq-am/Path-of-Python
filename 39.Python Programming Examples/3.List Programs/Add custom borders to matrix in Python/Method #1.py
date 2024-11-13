# Python3 code to demonstrate working of
# Custom Matrix Borders
# Using loop

# initializing list
test_list = [[4, 5, 6], [1, 4, 5],
			[6, 9, 1], [0, 3, 1]]

# printing original list
print("The original list is : " + str(test_list))

# initializing border
bord = "|"

for sub in test_list:
	temp = bord + " "

	# inner row
	for ele in sub:
		temp = temp + str(ele) + " "

	# adding border
	temp = temp + bord
	print(temp)
