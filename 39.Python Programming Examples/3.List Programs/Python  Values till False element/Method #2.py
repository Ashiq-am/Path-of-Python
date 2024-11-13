# Python3 code to demonstrate
# Values till False element
# using filter() + lamda + index()

# initializing list
test_list = [ 1, 5, 0, 0, 6]

# printing original list
print ("The original list is : " + str(test_list))

# Values till False element
# using filter() + lamda + index()
res = test_list.index(next(filter(lambda i: i == 0, test_list)))

# printing result
print ("The values till first False value : " + str(res))
