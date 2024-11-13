# Python3 code to demonstrate working of
# Reversing a range
# Using list split + slicing

# initializing list
test_list = [6, 3, 1, 8, 9, 2, 10, 12, 7, 4, 11]

# printing original list
print("The original list is : " + str(test_list))

# initializing range
strt, end = 3, 9

# Third arg. of split with -1 performs reverse
test_list[strt:end] = test_list[strt:end][::-1]

# printing result
print("Range reversed range list : " + str(test_list))
