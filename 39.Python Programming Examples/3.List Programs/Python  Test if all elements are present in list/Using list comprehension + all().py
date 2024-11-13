# Python3 code to demonstrate working of
# Test if all elements are present in list
# Using list comprehension + all()

# initializing list
target_list = [6, 4, 8, 9, 10]

# initializing test list
test_list = [4, 6, 9]

# printing lists
print("The target list : " + str(target_list))
print("The test list : " + str(test_list))

# Test if all elements are present in list
# Using list comprehension + all()
res = all(ele in target_list for ele in test_list)

# Printing result
print("Does every element of test_list is in target_list ? : " + str(res))
