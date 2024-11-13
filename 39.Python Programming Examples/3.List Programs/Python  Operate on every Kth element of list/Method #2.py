# Python3 code to demonstrate
# Edit every Kth element in list
# using list comprehension + list slicing

# initializing list
test_list = [1, 4, 5, 6, 7, 8, 9, 12]

# printing the original list
print ("The original list is : " + str(test_list))

# using list comprehension + list slicing
# Edit every Kth element in list
# add 2 to every 3rd element
test_list[0::3] = [i + 2 for i in test_list[0 :: 3]]

# printing result
print ("The list after editing every kth element : "
								+ str(test_list))
