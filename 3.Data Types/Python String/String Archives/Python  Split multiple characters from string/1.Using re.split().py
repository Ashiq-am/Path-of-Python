# Python3 code to demonstrate working of
# Splitting operators in String
# Using re.split()

import re

# initializing string
data = "GeeksforGeeks, is_an-awesome ! website"

# printing original string
print("The original string is : " + data)

# Using re.split()
# Splitting characters in String
res = re.split(', |_|-|!', data)

# printing result
print("The list after performing split functionality : " + str(res))
