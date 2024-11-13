# Python program to extract numeric digit
# from A string by regular expression...

# Importing module required for regular
# expressions
import re

# Example String
s = 'My 2 favourite numbers are 7 and 10'

# find all function to select all digit from 0
# to 9 [0-9] for numeric Letter in the String
# + for repeats a character one or more times
lst = re.findall('[0-9]+', s)

# Printing of List
print(lst)
