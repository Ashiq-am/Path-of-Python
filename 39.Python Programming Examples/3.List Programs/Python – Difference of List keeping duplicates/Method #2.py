# Python3 code to demonstrate
# Difference of List keeping duplicates
# using pop() + list comprehension + index()

# Initializing lists
test_list1 = [4, 5, 7, 4, 3]
test_list2 = [7, 3, 4]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Difference of List keeping duplicates
# using pop() + list comprehension + index()
[test_list1.pop(test_list1.index(idx)) for idx in test_list2]

# printing result
print ("List after performing difference : " + str(test_list1))
