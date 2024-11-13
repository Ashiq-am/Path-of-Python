# Python3 code to demonstrate working of
# Words with both alphabets and numbers
# Using regex
import re

# initializing string
test_str = 'geeksfor23geeks is best45 for gee34ks and cs'

# printing original string
print("The original string is : " + test_str)

# Words with both alphabets and numbers
# Using regex
res = re.findall(r'(?:\d+[a-zA-Z]+|[a-zA-Z]+\d+)', test_str)

# printing result
print("Words with alphabets and numbers : " + str(res))
