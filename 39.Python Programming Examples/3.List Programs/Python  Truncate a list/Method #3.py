# Python3 code to demonstrate
# to truncate list
# using list slicing

# initializing list
test_list = [1, 4, 5, 6, 7, 3, 8, 9, 10]

# printing original list
print ("The original list is : " + str(test_list))

# size desired
k = 5

# using list slicing
# to truncate list
res = test_list[0 : 5]

# printing result
print ("The truncated list is : " + str(res))
