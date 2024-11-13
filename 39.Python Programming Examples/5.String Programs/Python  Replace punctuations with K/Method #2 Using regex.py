# Python3 code to demonstrate working of
# Replace punctuations with K
# Using regex
import re

# initializing string
test_str = 'geeksforgeeks, is : best for ; geeks !!'

# printing original string
print("The original string is : " + str(test_str))

# initializing replace character
repl_char = '*'

# Replace punctuations with K
# Using regex
res = re.sub(r'[^\w\s]', repl_char, test_str)

# printing result
print("The strings after replacement : " + res)
