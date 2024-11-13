# Python3 code to demonstrate working of
# Eliminate Capital Letter Starting words from String
# Using regex()
import re

# initializing string
test_str = 'GeeksforGeeks is Best for Geeks'

# printing original string
print("The original string is : " + str(test_str))

# Eliminate Capital Letter Starting words from String
# Using regex()
res = re.sub(r"\s*[A-Z]\w*\s*", " ", test_str).strip()

# printing result
print("The filtered string : " + str(res))
