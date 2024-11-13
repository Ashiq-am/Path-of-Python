# Python3 code to demonstrate
# shift last element to first
# using list slicing and "+" operator

# initializing list
test_list = [1, 4, 5, 6, 7, 8, 9, 12]

# printing the original list
print ("The original list is : " + str(test_list))

# using list slicing and "+" operator
# shift last element to first
test_list = test_list[-1:] + test_list[:-1]

# printing result
print ("The list after shift is : " + str(test_list))
