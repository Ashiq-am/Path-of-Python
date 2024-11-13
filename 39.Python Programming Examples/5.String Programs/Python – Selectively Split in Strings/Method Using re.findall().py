# Python3 code to demonstrate working of
# Selective Split in Strings
# Using regex
import re

# initializing string
test_str = "print(\"geeks\");"

# printing original string
print("The original string is : " + test_str)

# Selective Split in Strings
# Using regex
res = re.findall('\d+\.\d+|\d+|\w+|[^a-zA-Z\s]', test_str)

# printing result
print("The splitted string is : " + str(res))
