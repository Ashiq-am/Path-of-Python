# Python code to demonstrate working of
# Replace multiple characters at once
# Using translate() + maketrans()
import string

# initializing string
test_str = "abbabba"

# printing original string
print("The original string is : " + str(test_str))

# Using translate() + maketrans()
# Replace multiple characters at once
res = test_str.translate(string.maketrans("ab", "ba"))

# printing result
print("The string after replacement of positions : " + res)
