# Python3 code to demonstrate working of
# Edit objects inside tuple
# Using Access Methods

# initializing tuple
test_tuple = (1, [5, 6, 4], 9, 10)

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Edit objects inside tuple
# Using Access Methods
test_tuple[1][2] = 14

# printing result
print("The modified tuple : " + str(test_tuple))
