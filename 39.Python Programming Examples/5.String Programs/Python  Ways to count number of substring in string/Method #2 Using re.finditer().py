# Python code to demonstrate
# to count total number
# of substring in string

import re
# Initialising string
ini_str = "ababababa"
sub_str = 'aba'

# Count count of substrings using re.finditer
res = sum(1 for _ in re.finditer('(?= aba)', ini_str))

# Printing result
print("Number of substrings", res)
