# Python3 code to demonstrate
# Shift from Front to Rear in List
# using insert() + pop()

# initializing list
test_list = [1, 4, 5, 6, 7, 8, 9, 12]

# printing the original list
print ("The original list is : " + str(test_list))

# using insert() + pop()
# Shift from Front to Rear in List
test_list.insert(len(test_list) - 1, test_list.pop(0))

# printing result
print ("The list after shift is : " + str(test_list))
