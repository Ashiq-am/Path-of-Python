# Python3 code to demonstrate working of
# Boolean List AND and OR operations
# OR operation - Using any()

# initialize list
test_list = [True, True, False, True, False]

# printing original list
print("The original list is : " + str(test_list))

# Boolean List AND and OR operations
# OR operation - Using any()
res = any(test_list)

# printing result
print("Result after performing OR among elements : " + str(res))
