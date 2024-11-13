# Python3 code to demonstrate
# to get first and last element of list
# using List slicing

# initializing list
test_list = [1, 5, 6, 7, 4]

# printing original list
print ("The original list is : " + str(test_list))

# using List slicing
# to get first and last element of list
res = test_list[::len(test_list)-1]

# printing result
print ("The first and last element of list are : " + str(res))
