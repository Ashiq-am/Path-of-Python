# Python3 code to demonstrate
# swapping sublist
# using list swapping and slicing

# initializing list
test_list = [1, 4, 5, 8, 3, 10, 6, 7, 11, 14, 15, 2]

# printing the original list
print ("The original list is : " + str(test_list))

# using list swapping and slicing
# swapping sublist
test_list[1 : 3], test_list[6 : 8] = test_list[6 : 8], test_list[1 : 3]

# printing result
print ("The list after sublist swapping : " + str(test_list))
