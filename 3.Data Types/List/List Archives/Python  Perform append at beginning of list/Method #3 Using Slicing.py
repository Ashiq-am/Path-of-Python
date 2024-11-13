# Python3 code to demonstrate
# to add element at beginning
# using slicing

# initializing list
test_list = [1, 3, 4, 5, 7]

# printing initial list
print("Original list : " + str(test_list))

# using slicing to append
# at beginning. append 6
test_list[:0] = [6]

# printing resultant list
print("Resultant list is : " + str(test_list))
