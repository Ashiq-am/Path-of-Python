# Python3 code to demonstrate working of
# Reverse Slicing string
# Using join() + reversed()

# initializing string
test_str = "GeeksforGeeks"

# printing original string
print("The original string is : " + test_str)

# initializing K
K = 7

# Using join() + reversed()
# Reverse Slicing string
res = ''.join(reversed(test_str[0:K]))

# printing result
print("The reversed sliced string is : " + res)
