# Python3 code to demonstrate
# to extract words from string
# using regex( findall() )
import re

# initializing string
test_string = "GeeksforGeeks is a computer science portal for Geeks !!!"

# printing original string
print("The original string is : " + test_string)

# using regex( findall() )
# to extract words from string
res = re.findall(r'\w+', test_string)

# printing result
print("\nThe words of string are")
for i in res:
    print(i)
