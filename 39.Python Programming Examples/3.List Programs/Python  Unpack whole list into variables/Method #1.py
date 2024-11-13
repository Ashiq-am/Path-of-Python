# Python3 code to demonstrate working of
# Unpack whole list into variables
# using "=" operator

# initialize list
test_list = [1, 3, 7, 4, 2]

# printing original list
print("The original list is : " + str(test_list))

# Unpack whole list into variables
# using "=" operator
one, two, three, four, five = test_list

# printing result
print("Variables as assigned are : " + str(one) + " "
									+ str(two) + " "
									+ str(three) + " "
									+ str(four) + " "
									+ str(five))
