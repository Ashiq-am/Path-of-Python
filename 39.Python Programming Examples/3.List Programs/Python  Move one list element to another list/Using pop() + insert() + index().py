# Python3 code to demonstrate working of
# Move one list element to another list
# Using pop() + index() + insert()

# initializing lists
test_list1 = [4, 5, 6, 7, 3, 8]
test_list2 = [7, 6, 3, 8, 10, 12]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Using pop() + index() + insert()
# Move one list element to another list
res = test_list1.insert(4, test_list2.pop(test_list2.index(10)))

# Printing result
print("The list 1 after insert is : " + str(test_list1))
print("The list 2 after remove is : " + str(test_list2))
