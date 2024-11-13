# Python3 code to demonstrate
# Words lengths in String
# using regex( findall() )
import re

# initializing string
test_string = "Geeksforgeeks, is best @# Computer Science Portal.!!!"

# printing original string
print ("The original string is : " + test_string)

# using regex( findall() )
# Words lengths in String
res = list(map(len, re.findall(r'\w+', test_string)))

# printing result
print ("The list of words lengths is : " + str(res))
