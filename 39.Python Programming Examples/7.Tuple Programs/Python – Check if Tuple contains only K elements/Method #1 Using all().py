# Python3 code to demonstrate working of
# Check if Tuple contains only K elements
# Using all()

# initializing tuple
test_tuple = (3, 5, 6, 5, 3, 6)

# printing original tuple
print("The original tuple : " + str(test_tuple))

# initializing K elements
K = [3, 6, 5]

# Check if Tuple contains only K elements
# Using all()
res = all(ele in K for ele in test_tuple)

# printing result
print("Does tuples contains just from K elements : " + str(res))
