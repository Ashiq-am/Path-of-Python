# Python3 code to demonstrate working of
# Uppercase Selective Substrings in String
# Using split() + join() + loop

# initializing strings
test_str = 'geeksforgeeks is best for cs'

# printing original string
print("The original string is : " + str(test_str))

# initializing substrings
sub_list = ["best", "cs", "geeksforgeeks"]

for sub in sub_list:
    # splitting string
    temp = test_str.split(sub, -1)

    # joining after uppercase
    test_str = sub.upper().join(temp)

# printing result
print("The String after uppercasing : " + str(test_str))
