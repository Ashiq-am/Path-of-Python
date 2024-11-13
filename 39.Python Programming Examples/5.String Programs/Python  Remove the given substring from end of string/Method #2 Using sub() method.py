# Python3 code to demonstrate
# to remove a substring from end of string

import re

# Initialising string
ini_string = 'xbzefdgstb'

# initializing string
sstring = 'stb'

# printing initial string and substring
print ("initial_strings : ", ini_string, "\nsubstring : ", sstring)

# removing substring from end
# of string using sub Method
if ini_string.endswith(sstring):
	res = re.sub(sstring, '', ini_string)

# printing result
print ("resultant string", res)
