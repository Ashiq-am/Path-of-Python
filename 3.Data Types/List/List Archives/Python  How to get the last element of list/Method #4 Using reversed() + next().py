# Python3 code to demonstrate
# accessing last element of list
# using reversed() + next()

# initializing list
test_list = [1, 4, 5, 6, 3, 5]

# printing original list
print ("The original list is : " + str(test_list))

# using reversed() + next() to print last element
print ("The last element using reversed() + next() is : "
						+ str(next(reversed(test_list))))
