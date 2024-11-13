# Python3 code to demonstrate
# to get index and value
# using enumerate

# initializing list
test_list = [1, 4, 5, 6, 7]

# Printing list
print ("Original list is : " + str(test_list))

# using enumerate to
# get index and value
print ("List index-value are : ")
for index, value in enumerate(test_list):
	print(index, value)
