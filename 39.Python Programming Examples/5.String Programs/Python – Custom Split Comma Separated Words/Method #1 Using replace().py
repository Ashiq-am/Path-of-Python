# Python3 code to demonstrate working of
# Custom Split Comma Separated Words
# Using replace()

# initializing string
test_str = 'geeksforgeeks, is, best, for, geeks'

# printing original string
print("The original string is : " + str(test_str))

# Distance between occurrences
# Using replace()
res = test_str.replace(", ", " , ").split()

# printing result
print("The strings after performing splits : " + str(res))
