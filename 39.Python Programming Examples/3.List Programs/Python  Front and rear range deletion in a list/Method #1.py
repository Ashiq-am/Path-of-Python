# Python3 code to demonstrate
# front and rear deletion
# using del operator + list slicing

# initializing list
test_list = [2, 3, 5, 7, 9, 10, 8, 6]

# printing original list
print ("The original list is : " + str(test_list))

# using del operator + list slicing
# front and rear deletion
del test_list[-2:], test_list[:2]

# printing result
print ("The cropped list is : " + str(test_list))
