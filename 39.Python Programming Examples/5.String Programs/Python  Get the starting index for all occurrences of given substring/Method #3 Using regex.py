# Python3 code to demonstrate
# to find all occurrences of substring in
# a string
import re

# Initialising string
ini_string = 'xbzefdgstbzefzexezef'

# Initialising sub-string
sub_string = 'zef'

# Printing initial string and sub-string
print ("initial_strings : ", ini_string, "\nsubstring : ", sub_string)

res = []
# Finding all occurrences of substring
# in a string using re.finditer
res = [m.start() for m in re.finditer(sub_string, ini_string)]

# printing result(
print ("resultant positions", str(res))
