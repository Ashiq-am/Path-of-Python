# Python3 code to demonstrate
# shift last element to first
# using insert() + pop()

# initializing list
test_list = [1, 4, 5, 6, 7, 8, 9, 12]

# printing the original list
print ("The original list is : " + str(test_list))

# using insert() + pop()
# shift last element to first
test_list.insert(0, test_list.pop())

# printing result
print ("The list after shift is : " + str(test_list))
