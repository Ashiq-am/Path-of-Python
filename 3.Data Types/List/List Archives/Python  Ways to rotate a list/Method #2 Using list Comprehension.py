# Python3 code to demonstrate
# rotation of list
# using list comprehension

# initializing list
test_list = [1, 4, 6, 7, 2]

# printing original list
print ("Original list : " + str(test_list))

# using list comprehension to left rotate by 3
test_list = [test_list[(i + 3) % len(test_list)]
			for i, x in enumerate(test_list)]

# Printing list after left rotate
print ("List after left rotate by 3 : " + str(test_list))

# using list comprehension to right rotate by 3
# back to Original
test_list = [test_list[(i - 3) % len(test_list)]
			for i, x in enumerate(test_list)]

# Printing after right rotate
print ("List after right rotate by 3(back to original) : "
										+ str(test_list))
