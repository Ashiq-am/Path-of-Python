# Python 3 code to demonstrate
# Union Operation in two Strings
# using set() + union()

# initializing strings
test_str1 = 'GeeksforGeeks'
test_str2 = 'Codefreaks'

# Printing initial strings
print("The original string 1 is : " + test_str1)
print("The original string 2 is : " + test_str2)

# using set() + union() to
# Union Operation in two Strings
res = set(test_str1).union(test_str2)

# printing result
print("The string union is : " + str(res))
