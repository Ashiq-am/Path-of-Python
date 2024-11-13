# Python3 code to demonstrate working of
# Test if Kth character is digit in String
# Using isdigit()

# initializing string
test_str = 'geeks4geeks'

# printing original String
print("The original string is : " + str(test_str))

# initializing K
K = 5

# isdigit checks for digit
res = test_str[K].isdigit()

# printing result
print("Is Kth element String : " + str(res))
