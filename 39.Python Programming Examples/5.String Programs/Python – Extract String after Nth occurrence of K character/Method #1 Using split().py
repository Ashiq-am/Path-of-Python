# Python3 code to demonstrate working of
# Extract String after Nth occurrence of K character
# Using split()

# initializing string
test_str = 'geekforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = "e"

# initializing N
N = 3

# using split() to perform required string split
# "-1" to extract required part
res = test_str.split(K, N)[-1]

# printing result
print("The extracted string : " + str(res))
