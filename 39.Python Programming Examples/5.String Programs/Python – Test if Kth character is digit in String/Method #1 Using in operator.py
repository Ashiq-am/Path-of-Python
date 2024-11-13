# Python3 code to demonstrate working of
# Test if Kth charater is digit in String
# Using in operator

# initializing string
test_str = 'geeks4geeks'

# printing original String
print("The original string is : " + str(test_str))

# initializing K
K = 5

# checking if Kth digit is string
# getting numeric str
num_str = "0123456789"
res = test_str[K] in num_str

# printing result
print("Is Kth element String : " + str(res))
