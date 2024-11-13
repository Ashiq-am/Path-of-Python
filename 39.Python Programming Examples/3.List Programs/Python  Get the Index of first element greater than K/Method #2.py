# Python3 code to demonstrate
# to find index of first element just
# greater than K
# using filter() + lambda

# initializing list
test_list = [0.4, 0.5, 11.2, 8.4, 10.4]

# printing original list
print ("The original list is : " + str(test_list))

# using filter() + lambda
# to find index of first element just
# greater than 0.6
res = list(filter(lambda i: i > 0.6, test_list))[0]

# printing result
print ("The index of element just greater than 0.6 : "
						+ str(test_list.index(res)))
