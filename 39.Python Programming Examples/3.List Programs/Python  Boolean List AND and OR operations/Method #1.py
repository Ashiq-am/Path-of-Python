# Python3 code to demonstrate working of
# Boolean List AND and OR operations
# AND Operation - Using all()

# initialize list
test_list = [True, True, False, True, False]

# printing original list
print("The original list is : " + str(test_list))

# Boolean List AND and OR operations
# AND Operation - Using all()
res = all(test_list)

# printing result
print("Result after performing AND among elements : " + str(res))
