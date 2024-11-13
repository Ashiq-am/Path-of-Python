# Python3 code to demonstrate working of
# Initial character upper case
# Using upper() + string slicing

# initializing string
test_str = "geeksforgeeks"

# printing original string
print("The original string is : " + str(test_str))

# Using upper() + string slicing
# Initial character upper case
res = test_str[0].upper() + test_str[1:]

# printing result
print("The string after uppercasing initial character : " + str(res))
