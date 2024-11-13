# Python3 code to demonstrate
# Test if all elements in list are of same type
# using all() + isinstance()

# Initializing lists
test_list = [5, 6, 2, 5, 7, 9]

# printing original list
print("The original list is : " + str(test_list))

# Test if all elements in list are of same type
# using all() + isinstance()
res = all(isinstance(sub, type(test_list[0])) for sub in test_list[1:])

# printing result
print ("Do all elements have same type : " + str(res))
