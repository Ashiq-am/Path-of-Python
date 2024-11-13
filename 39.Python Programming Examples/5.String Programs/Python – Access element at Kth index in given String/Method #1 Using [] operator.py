# Python3 code to demonstrate working of
# Access element at Kth index in String
# Using []

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 7

# try-except block for error handling
try:

    # access Kth element
    res = test_str[K]
except Exception as e:
    res = str(e)

# printing result
print("Kth index element : " + str(res))
