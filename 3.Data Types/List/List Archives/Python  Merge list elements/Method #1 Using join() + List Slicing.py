# Python3 code to demonstrate
# merging list elements
# using join() + list slicing

# initializing list
test_list = ['I', 'L', 'O', 'V', 'E', 'G', 'F', 'G']

# printing original list
print ("The original list is : " + str(test_list))

# using join() + list slicing
# merging list elements
test_list[5 : 8] = [''.join(test_list[5 : 8])]

# printing result
print ("The list after merging elements : " + str(test_list))
