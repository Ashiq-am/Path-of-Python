# Python3 code to demonstrate
# to count words in string
# using regex (findall())
import re

# initializing string
test_string = "Geeksforgeeks, is best @# Computer Science Portal.!!!"

# printing original string
print ("The original string is : " + test_string)

# using regex (findall())
# to count words in string
res = len(re.findall(r'\w+', test_string))

# printing result
print ("The number of words in string are : " + str(res))
