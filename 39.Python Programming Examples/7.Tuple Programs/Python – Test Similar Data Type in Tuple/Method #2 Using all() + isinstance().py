# Python3 code to demonstrate working of
# Test Similar Data Type in Tuple
# Using all() + isinstance()

# initializing tuple
test_tuple = (5, 6, 7, 3, 5, 6)

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Test Similar Data Type in Tuple
# Using all() + isinstance()
res = all(isinstance(ele, type(test_tuple[0])) for ele in test_tuple)

# printing result
print("Do all elements have same type ? : " + str(res))
