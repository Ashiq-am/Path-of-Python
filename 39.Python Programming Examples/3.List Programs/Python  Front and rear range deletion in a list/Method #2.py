# Python3 code to demonstrate
# front and rear deletion
# using list slicing

# initializing list
test_list = [2, 3, 5, 7, 9, 10, 8, 6]

# printing original list
print ("The original list is : " + str(test_list))

# using list slicing
# front and rear deletion
res = test_list[2 : -2]

# printing result
print ("The cropped list is : " + str(res))
