# Python3 code to demonstrate
# deleting columns of list of lists
# using pop() + list comprehension

# initializing list
test_list = [[4, 5, 6, 8],
			[2, 7, 10, 9],
			[12, 16, 18, 20]]

# printing original list
print ("The original list is : " + str(test_list))

# using pop() + list comprehension
# deleting column element of row
[j.pop(1) for j in test_list]

# printing result
print ("The modified mesh after column deletion : " + str(test_list))
