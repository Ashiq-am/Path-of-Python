# Python3 code to demonstrate
# finding first True value
# using filter() + lamda + index()

# initializing list
test_list = [ 0, 0, 5, 6, 0]

# printing original list
print ("The original list is : " + str(test_list))

# finding first True value
# using filter() + lamda + index()
res = test_list.index(next(filter(lambda i: i != 0, test_list)))

# printing result
print ("The values till first True value : " + str(res))
