# Python code to demonstrate
# to count total number
# of substring in string

import re
# Initialising string
ini_str = "ababababa"
sub_str = 'aba'

# Count count of substrings using re.findall
res = len(re.findall('(?= aba)', ini_str))

# Printing result
print("Number of substrings", res)
