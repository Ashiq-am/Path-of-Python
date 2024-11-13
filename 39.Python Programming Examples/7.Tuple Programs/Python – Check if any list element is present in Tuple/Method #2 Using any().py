# Python3 code to demonstrate working of
# Check if any list element is present in Tuple
# Using any()

# initializing tuple
test_tup = (4, 5, 7, 9, 3)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# initializing list
check_list = [6, 7, 10, 11]

# generator expression is used for iteration
res = any(ele in test_tup for ele in check_list)

# printing result
print("Is any list element present in tuple ? : " + str(res))
