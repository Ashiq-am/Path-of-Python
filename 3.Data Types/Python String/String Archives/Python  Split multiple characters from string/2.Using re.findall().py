# Python3 code to demonstrate working of
# Splitting operators in String
# Using re.findall()
import re


# initializing string
data = "This, is - another : example?!"

# printing original string
print("The original string is : " + data)

# Using re.findall()
# Splitting characters in String
res = re.findall(r"[\w']+", data)

# printing result
print("The list after performing split functionality : " + str(res))
