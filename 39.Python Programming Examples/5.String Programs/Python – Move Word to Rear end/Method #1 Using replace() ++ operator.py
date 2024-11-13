# Python3 code to demonstrate working of
# Move Word to Rear end
# Using replace() + "+" operator

# initializing string
test_str = 'Geeksforgeeks is best for geeks '

# printing original string
print("The original string is : " + str(test_str))

# initializing Substring
sub_str = 'best'

# Move Word to Rear end
# Using replace() + "+" operator
res = test_str.replace(sub_str, "") + str(sub_str)

# printing result
print("The string after word removal : " + str(res))
