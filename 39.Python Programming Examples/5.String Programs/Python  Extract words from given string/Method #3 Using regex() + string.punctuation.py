# Python3 code to demonstrate
# to extract words from string
# using regex() + string.punctuation
import re
import string

# initializing string
test_string = "Geeksforgeeks, is best @# Computer Science Portal.!!!"

# printing original string
print ("The original string is : " + test_string)

# using regex() + string.punctuation
# to extract words from string
res = re.sub('['+string.punctuation+']', '', test_string).split()

# printing result
print ("The list of words is : " + str(res))
